import yaml
import requests
import subprocess
import time
import logging
from datetime import datetime, timedelta
from requests.exceptions import RequestException
import ipaddress
import socket
import os

# Set up logging
if not os.path.exists("/app/logs/network_monitor.log"):
    with open("/app/logs/network_monitor.log", "w") as f:
        f.write("*****************\n")

logging.basicConfig(
    filename="/app/logs/network_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def ping(host):
    try:
        subprocess.check_output(["ping", "-c", "1", "-W", "1", host])
        return True
    except subprocess.CalledProcessError:
        return False


def check_http(url, error_content=None):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return False
        if error_content and error_content in response.text:
            return False
        return True
    except RequestException:
        return False


def update_home_assistant(ha_config, entity_id, state):
    url = f"{ha_config['url']}/api/states/{entity_id}"
    headers = {
        "Authorization": f"Bearer {ha_config['token']}",
        "Content-Type": "application/json",
    }
    data = {"state": state}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        logging.info(f"Successfully updated {entity_id} to {state}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to update Home Assistant: {e}")


def check_target(target):
    if target["type"] == "ping":
        return ping(target["host"])
    elif target["type"] == "http":
        return check_http(target["url"], target.get("error_content"))


def get_interval(target, default_interval):
    if "check_interval" in target:
        return timedelta(**target["check_interval"])
    return default_interval


def discover_hosts(ip_ranges):
    discovered_hosts = []
    for ip_range in ip_ranges:
        start_ip = ipaddress.ip_address(ip_range["start"])
        end_ip = ipaddress.ip_address(ip_range["end"])
        for ip in range(int(start_ip), int(end_ip) + 1):
            host = str(ipaddress.ip_address(ip))
            if ping(host):
                try:
                    hostname = socket.gethostbyaddr(host)[0]
                except socket.herror:
                    hostname = host
                discovered_hosts.append(
                    {
                        "name": f"Discovered {hostname}",
                        "type": "ping",
                        "host": host,
                        "entity_id": f"binary_sensor.discovered_{host.replace('.', '_')}",  # noqa: E501
                    }
                )
    return discovered_hosts


def update_config(config, discovered_hosts):
    existing_hosts = {
        target["host"] for target in config["targets"] if "host" in target
    }
    new_hosts = [
        host for host in discovered_hosts if host["host"] not in existing_hosts
    ]

    if new_hosts:
        config["targets"].extend(new_hosts)
        with open("/app/config.yml", "w") as config_file:
            yaml.dump(config, config_file, line_break="\n\n")
        logging.info(f"Added {len(new_hosts)} new hosts to the configuration")


def main():
    with open("/app/config.yml", "r") as config_file:
        config = yaml.safe_load(config_file)

    default_interval = timedelta(**config["default_check_interval"])
    next_checks = {target["name"]: datetime.now()
                   for target in config["targets"]}
    last_discovery = datetime.now() - timedelta(**config["discovery"]["interval"])  # noqa: E501

    while True:
        now = datetime.now()

        # Run discovery if enabled and it's time
        if config["discovery"]["enabled"] and now - last_discovery >= timedelta(  # noqa: E501
            **config["discovery"]["interval"]
        ):
            logging.info("Running network discovery")
            discovered_hosts = discover_hosts(config["discovery"]["ip_ranges"])
            update_config(config, discovered_hosts)
            last_discovery = now

        for target in config["targets"]:
            if now >= next_checks.get(target["name"], now):
                result = check_target(target)
                logging.info(f"Check result for {target['name']}: {result}")
                update_home_assistant(
                    config["home_assistant"],
                    target["entity_id"],
                    "on" if result else "off",
                )

                interval = get_interval(target, default_interval)
                next_checks[target["name"]] = now + interval
                logging.info(
                    f"Next check for {target['name']} scheduled for {next_checks[target['name']]}"  # noqa: E501
                )

        # Sleep for a short time before checking again
        time.sleep(10)


if __name__ == "__main__":
    main()
