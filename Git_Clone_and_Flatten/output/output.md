# setup.py
```python
#!/usr/bin/env python
"""This module contains setup instructions for pytube."""
import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open(os.path.join(here, "pytube", "version.py")) as fp:
    exec(fp.read())

setup(
    name="pytube",
    version=__version__,  # noqa: F821
    author="Ronnie Ghose, Taylor Fox Dahlin, Nick Ficano",
    author_email="hey@pytube.io",
    packages=["pytube", "pytube.contrib"],
    package_data={"": ["LICENSE"],},
    url="https://github.com/pytube/pytube",
    license="The Unlicense (Unlicense)",
    entry_points={
        "console_scripts": [
            "pytube = pytube.cli:main"],},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    description=("Python 3 library for downloading YouTube Videos."),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description=long_description,
    zip_safe=True,
    python_requires=">=3.7",
    project_urls={
        "Bug Reports": "https://github.com/pytube/pytube/issues",
        "Read the Docs": "https://pytube.io",
    },
    keywords=["youtube", "download", "video", "stream",],
)

```

# Contributing.md
```markdown
## How to contribute to Pytube

#### **Did you find a bug?**

* **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/pytube/pytube/issues).

* If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/pytube/pytube/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **[MRE code sample](https://stackoverflow.com/help/minimal-reproducible-example)** or an **executable test case** demonstrating the expected behavior that is not occurring.

* For more detailed information on submitting a bug report and creating an issue, visit `TODO`

#### **Did you write a patch that fixes a bug?**

* Open a new GitHub pull request with the patch.

* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

* Before submitting, please read the [Numpy Contribution Guidelines](https://numpy.org/devdocs/dev/index.html) guide to know more about coding conventions and benchmarks.

#### **Did you fix whitespace, format code, or make a purely cosmetic patch?**

Changes that are cosmetic in nature and do not add anything substantial to the stability, functionality, or testability of Pytube will generally not be accepted as we abide by pep8 formatting.

#### **Do you intend to add a new feature or change an existing one?**

* Suggest your change as an issue in the with the label #enhancement

* Though perhaps not common as GitHub issues are primarily intended for bug reports and fixes, PyTube is currently using issues for open design proposals.

#### **Do you have questions about the source code?**

* Ask any question about how to use PyTube [in StackOverflow](https://stackoverflow.com/questions/tagged/pytube)

#### **Do you want to contribute to the PyTube documentation?**

* Consider submitting a patch to the [docs](https://github.com/pytube/pytube/tree/master/docs)

PyTube is a volunteer effort. We encourage you to pitch in and [join the team](https://contributors.rubyonrails.org)!

Thanks! :smile: :heart:

PyTube Team

```

# .pre-commit-config.yaml
```yaml
repos:
  - repo: 'https://github.com/pre-commit/pre-commit-hooks'
    rev: v3.1.0
    hooks:
      - id: pretty-format-json
        name: 'Pretty format JSON'
        args:
          - '--no-sort-keys'
          - '--autofix'
          - '--indent=2'
      - id: trailing-whitespace
        name: 'Fix trailing whitespace'
        exclude: setup.cfg
      - id: end-of-file-fixer
        name: 'Fix missing EOF'
        exclude: setup.cfg
      - id: check-executables-have-shebangs
        name: 'Check exeutables for shebangs'
      - id: check-merge-conflict
        name: 'Check for merge conflict fragments'
      - id: check-case-conflict
        name: 'Check for filesystem character case conflicts'
      - id: detect-private-key
        name: 'Check for cleartext private keys stored'
      - id: check-json
        name: 'Validate JSON'
      - id: check-ast
        name: 'Check Python abstract syntax tree'
  - repo: 'https://github.com/asottile/reorder_python_imports'
    rev: v1.8.0
    hooks:
      - id: reorder-python-imports
        name: 'Reorder Python imports'
  - repo: 'https://github.com/pre-commit/mirrors-autopep8'
    rev: ''
    hooks:
      - id: autopep8
        name: 'Pretty format Python'
    args:
      - '--in-place'
      - '--aggressive'
      - '--aggressive'
      - '--experimental'
      - '--remove-all-unused-imports'
      - '--ignore-init-module-imports'
      - '--remove-unused-variable'
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
    - id: black
      name: 'Ruthlessly format Python'
      language_version: python3.7
      args:
        - '--line-length=79'

```

# .gitignore
```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Temp files
*~
~*
.*~
\#*
.#*
*#

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
*.mp4

# Performance profiling
prof/
*.cprof

# Debian Files
debian/files
debian/python-beaver*

# Sphinx build
doc/_build

# Generated man page
doc/aws_hostname.1

_run.py
_devfiles/*

_build
_static
_templates
_autosummary
.pytest_cache*

.vscode/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Mac
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon?
Icon


# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

.dropbox

# Generated
test/**/*.xml
/*.gv
/*.dot
/*.xml

# PyCharm
.idea/
.idea/workspace.xml
.idea/usage.statistics.xml
.idea/tasks.xml
.idea/modules.xml
.idea/*.iml

# Additional IDE files
*.sublime-project

# Common virtual environments
venv/
env/

# Token cache location
__cache__/
```

# .readthedocs.yml
```yaml
# .readthedocs.yml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: docs/conf.py

# Optionally build your docs in additional formats such as PDF and ePub
formats: all

# Optionally set the version of Python and requirements required to build your docs
python:
  version: 3.7
  install:
    - requirements: docs/requirements.txt

```

# .editorconfig
```editorconfig
root = true

[*]
indent_style = space
indent_size = 4
end_of_line = lf
trim_trailing_whitespace = true
insert_final_newline = true
charset = utf-8

[*.py]
max_line_length = 95

```

# README.md
```markdown
<div align="center">
  <p>
    <a href="#"><img src="https://assets.nickficano.com/gh-pytube.min.svg" width="456" height="143" alt="pytube logo" /></a>
  </p>
  <p align="center">
	<a href="https://pypi.org/project/pytube/"><img src="https://img.shields.io/pypi/dm/pytube?style=flat-square" alt="pypi"/></a>
	<a href="https://pytube.io/en/latest/"><img src="https://readthedocs.org/projects/python-pytube/badge/?version=latest&style=flat-square" /></a>
	<a href="https://pypi.org/project/pytube/"><img src="https://img.shields.io/pypi/v/pytube?style=flat-square" /></a>
  </p>
</div>

### Actively soliciting contributors!

Have ideas for how pytube can be improved? Feel free to open an issue or a pull request!

# pytube

*pytube* is a genuine, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

## Documentation

Detailed documentation about the usage of the library can be found at [pytube.io](https://pytube.io). This is recommended for most cases. If you want to hastily download a single video, the [quick start](#Quickstart) guide below might be what you're looking for.

## Description

YouTube is the most popular video-sharing platform in the world and as a hacker, you may encounter a situation where you want to script something to download videos. For this, I present to you: *pytube*.

*pytube* is a lightweight library written in Python. It has no third-party
dependencies and aims to be highly reliable.

*pytube* also makes pipelining easy, allowing you to specify callback functions for different download events, such as  ``on progress`` or ``on complete``.

Furthermore, *pytube* includes a command-line utility, allowing you to download videos right from the terminal.

## Features

- Support for both progressive & DASH streams
- Support for downloading the complete playlist
- Easily register ``on_download_progress`` & ``on_download_complete`` callbacks
- Command-line interfaced included
- Caption track support
- Outputs caption tracks to .srt format (SubRip Subtitle)
- Ability to capture thumbnail URL
- Extensively documented source code
- No third-party dependencies

## Quickstart

This guide covers the most basic usage of the library. For more detailed information, please refer to [pytube.io](https://pytube.io).

### Installation

Pytube requires an installation of Python 3.6 or greater, as well as pip. (Pip is typically bundled with Python [installations](https://python.org/downloads).)

To install from PyPI with pip:

```bash
$ python -m pip install pytube
```

Sometimes, the PyPI release becomes slightly outdated. To install from the source with pip:

```bash
$ python -m pip install git+https://github.com/pytube/pytube
```

### Using pytube in a Python script

To download a video using the library in a script, you'll need to import the YouTube class from the library and pass an argument of the video URL. From there, you can access the streams and download them.

```python
 >>> from pytube import YouTube
 >>> YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
 >>> yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
 >>> yt.streams
  ... .filter(progressive=True, file_extension='mp4')
  ... .order_by('resolution')
  ... .desc()
  ... .first()
  ... .download()
```

### Using the command-line interface

Using the CLI is remarkably straightforward as well. To download a video at the highest progressive quality, you can use the following command:
```bash
$ pytube https://youtube.com/watch?v=2lAe1cqCOXo
```

You can also do the same for a playlist:
```bash
$ pytube https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n
```

```

# CODE_OF_CONDUCT.md
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
github issue.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

# tests/test_exceptions.py
```python
import pytest
from unittest import mock

import pytube.exceptions as exceptions
from pytube import YouTube


def test_video_unavailable():
    try:
        raise exceptions.VideoUnavailable(video_id="YLnZklYFe7E")
    except exceptions.VideoUnavailable as e:
        assert e.video_id == "YLnZklYFe7E"  # noqa: PT017
        assert str(e) == "YLnZklYFe7E is unavailable"


def test_regex_match_error():
    try:
        raise exceptions.RegexMatchError(caller="hello", pattern="*")
    except exceptions.RegexMatchError as e:
        assert str(e) == "hello: could not find match for *"


def test_live_stream_error():
    # Ensure this can be caught as generic VideoUnavailable exception
    with pytest.raises(exceptions.VideoUnavailable):
        raise exceptions.LiveStreamError(video_id='YLnZklYFe7E')
    try:
        raise exceptions.LiveStreamError(video_id='YLnZklYFe7E')
    except exceptions.LiveStreamError as e:
        assert e.video_id == 'YLnZklYFe7E'  # noqa: PT017
        assert str(e) == 'YLnZklYFe7E is streaming live and cannot be loaded'


def test_recording_unavailable_error():
    # Ensure this can be caught as generic VideoUnavailable exception
    with pytest.raises(exceptions.VideoUnavailable):
        raise exceptions.RecordingUnavailable(video_id='5YceQ8YqYMc')
    try:
        raise exceptions.RecordingUnavailable(video_id='5YceQ8YqYMc')
    except exceptions.RecordingUnavailable as e:
        assert e.video_id == '5YceQ8YqYMc'  # noqa: PT017
        assert str(e) == '5YceQ8YqYMc does not have a live stream recording available'


def test_private_error():
    # Ensure this can be caught as generic VideoUnavailable exception
    with pytest.raises(exceptions.VideoUnavailable):
        raise exceptions.VideoPrivate('m8uHb5jIGN8')
    try:
        raise exceptions.VideoPrivate('m8uHb5jIGN8')
    except exceptions.VideoPrivate as e:
        assert e.video_id == 'm8uHb5jIGN8'  # noqa: PT017
        assert str(e) == 'm8uHb5jIGN8 is a private video'


def test_region_locked_error():
    # Ensure this can be caught as generic VideoUnavailable exception
    with pytest.raises(exceptions.VideoUnavailable):
        raise exceptions.VideoRegionBlocked('hZpzr8TbF08')
    try:
        raise exceptions.VideoRegionBlocked('hZpzr8TbF08')
    except exceptions.VideoRegionBlocked as e:
        assert e.video_id == 'hZpzr8TbF08'  # noqa: PT017
        assert str(e) == 'hZpzr8TbF08 is not available in your region'


def test_raises_video_private(private):
    with mock.patch('pytube.request.urlopen') as mock_url_open:
        # Mock the responses to YouTube
        mock_url_open_object = mock.Mock()
        mock_url_open_object.read.side_effect = [
            private['watch_html'].encode('utf-8'),
        ]
        mock_url_open.return_value = mock_url_open_object
        with pytest.raises(exceptions.VideoPrivate):
            YouTube('https://youtube.com/watch?v=m8uHb5jIGN8').streams


def test_raises_recording_unavailable(missing_recording):
    with mock.patch('pytube.request.urlopen') as mock_url_open:
        # Mock the responses to YouTube
        mock_url_open_object = mock.Mock()
        mock_url_open_object.read.side_effect = [
            missing_recording['watch_html'].encode('utf-8'),
        ]
        mock_url_open.return_value = mock_url_open_object
        with pytest.raises(exceptions.RecordingUnavailable):
            YouTube('https://youtube.com/watch?v=5YceQ8YqYMc').streams

```

# tests/conftest.py
```python
"""Reusable dependency injected testing components."""
import gzip
import json
import os
import pytest
from unittest import mock

from pytube import YouTube


def load_playback_file(filename):
    """Load a gzip json playback file."""
    cur_fp = os.path.realpath(__file__)
    cur_dir = os.path.dirname(cur_fp)
    fp = os.path.join(cur_dir, "mocks", filename)
    with gzip.open(fp, "rb") as fh:
        content = fh.read().decode("utf-8")
        return json.loads(content)


@mock.patch('pytube.request.urlopen')
def load_and_init_from_playback_file(filename, mock_urlopen):
    """Load a gzip json playback file and create YouTube instance."""
    pb = load_playback_file(filename)

    # Mock the responses to YouTube
    mock_url_open_object = mock.Mock()
    mock_url_open_object.read.side_effect = [
        pb['watch_html'].encode('utf-8'),
        pb['js'].encode('utf-8')
    ]
    mock_urlopen.return_value = mock_url_open_object

    # Pytest caches this result, so we can speed up the tests
    #  by causing the object to fetch all the relevant information
    #  it needs. Previously, this was handled by prefetch_init()
    #  and descramble(), but this functionality has since been
    #  deferred
    v = YouTube(pb["url"])
    v.watch_html
    v._vid_info = pb['vid_info']
    v.js
    v.fmt_streams
    return v


@pytest.fixture
def cipher_signature():
    """Youtube instance initialized with video id 2lAe1cqCOXo."""
    filename = "yt-video-2lAe1cqCOXo-html.json.gz"
    return load_and_init_from_playback_file(filename)


@pytest.fixture
def presigned_video():
    """Youtube instance initialized with video id QRS8MkLhQmM."""
    filename = "yt-video-QRS8MkLhQmM-html.json.gz"
    return load_and_init_from_playback_file(filename)


@pytest.fixture
def age_restricted():
    """Youtube instance initialized with video id irauhITDrsE."""
    filename = "yt-video-irauhITDrsE-html.json.gz"
    return load_playback_file(filename)


@pytest.fixture
def private():
    """Youtube instance initialized with video id m8uHb5jIGN8."""
    filename = "yt-video-m8uHb5jIGN8-html.json.gz"
    return load_playback_file(filename)


@pytest.fixture
def missing_recording():
    """Youtube instance initialized with video id 5YceQ8YqYMc."""
    filename = "yt-video-5YceQ8YqYMc-html.json.gz"
    return load_playback_file(filename)


@pytest.fixture
def playlist_html():
    """Youtube playlist HTML loaded on 2020-01-25 from
    https://www.youtube.com/playlist?list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr
    """
    file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "mocks",
        "playlist.html.gz",
    )
    with gzip.open(file_path, "rb") as f:
        return f.read().decode("utf-8")


@pytest.fixture
def playlist_long_html():
    """Youtube playlist HTML loaded on 2020-01-25 from
    https://www.youtube.com/playlist?list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr
    """
    file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "mocks",
        "playlist_long.html.gz",
    )
    with gzip.open(file_path, "rb") as f:
        return f.read().decode("utf-8")


@pytest.fixture
def playlist_submenu_html():
    """Youtube playlist HTML loaded on 2020-01-24 from
    https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr
    """
    file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "mocks",
        "playlist_submenu.html.gz",
    )
    with gzip.open(file_path, "rb") as f:
        return f.read().decode("utf-8")


@pytest.fixture
def stream_dict():
    """Youtube instance initialized with video id WXxV9g7lsFE."""
    file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "mocks",
        "yt-video-WXxV9g7lsFE-html.json.gz",
    )
    with gzip.open(file_path, "rb") as f:
        content = json.loads(f.read().decode("utf-8"))
        return content['watch_html']


@pytest.fixture
def channel_videos_html():
    """Youtube channel HTML loaded on 2021-05-05 from
    https://www.youtube.com/c/ProgrammingKnowledge/videos
    """
    file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "mocks",
        "channel-videos.html.gz",
    )
    with gzip.open(file_path, 'rb') as f:
        return f.read().decode('utf-8')


@pytest.fixture
def base_js():
    """Youtube base.js files retrieved on 2022-02-04 and 2022-04-15
    from https://www.youtube.com/watch?v=vmzxpUsN0uA and
    https://www.youtube.com/watch?v=Y4-GSFKZmEg respectively
    """
    base_js_files = []
    for file in ["base.js-2022-02-04.gz", "base.js-2022-04-15.gz"]:
        file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "mocks",
            file,
        )
        with gzip.open(file_path, 'rb') as f:
            base_js_files.append(f.read().decode('utf-8'))
    return base_js_files

```

# tests/__init__.py
```python
"""Package init | pydocstyle ignore isn't working :/."""

```

# tests/test_request.py
```python
import socket
import os
import pytest
from unittest import mock
from urllib.error import URLError

from pytube import request
from pytube.exceptions import MaxRetriesExceeded


@mock.patch("pytube.request.urlopen")
def test_streaming(mock_urlopen):
    # Given
    fake_stream_binary = [
        os.urandom(8 * 1024),
        os.urandom(8 * 1024),
        os.urandom(8 * 1024),
        None,
    ]
    mock_response = mock.Mock()
    mock_response.read.side_effect = fake_stream_binary
    mock_response.info.return_value = {"Content-Range": "bytes 200-1000/24576"}
    mock_urlopen.return_value = mock_response
    # When
    response = request.stream("http://fakeassurl.gov/streaming_test")
    # Then
    assert len(b''.join(response)) == 3 * 8 * 1024
    assert mock_response.read.call_count == 4


@mock.patch('pytube.request.urlopen')
def test_timeout(mock_urlopen):
    exc = URLError(reason=socket.timeout('timed_out'))
    mock_urlopen.side_effect = exc
    generator = request.stream('http://fakeassurl.gov/timeout_test', timeout=1)
    with pytest.raises(MaxRetriesExceeded):
        next(generator)


@mock.patch("pytube.request.urlopen")
def test_headers(mock_urlopen):
    response = mock.Mock()
    response.info.return_value = {"content-length": "16384"}
    mock_urlopen.return_value = response
    response = request.head("http://fakeassurl.gov")
    assert response == {"content-length": "16384"}


@mock.patch("pytube.request.urlopen")
def test_get(mock_urlopen):
    response = mock.Mock()
    response.read.return_value = "<html></html>".encode("utf-8")
    mock_urlopen.return_value = response
    response = request.get("http://fakeassurl.gov")
    assert response == "<html></html>"


def test_get_non_http():
    with pytest.raises(ValueError):  # noqa: PT011
        request.get("file://bad")

```

# tests/test_cli.py
```python
import argparse
import logging
import os
from unittest import mock
from unittest.mock import MagicMock, patch

import pytest

from pytube import Caption, CaptionQuery, cli, StreamQuery
from pytube.exceptions import PytubeError

parse_args = cli._parse_args


@mock.patch("pytube.cli._parse_args")
def test_main_invalid_url(_parse_args):  # noqa: PT019
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["crikey",],)
    _parse_args.return_value = args
    with pytest.raises(SystemExit):
        cli.main()


@mock.patch("pytube.cli.display_streams")
@mock.patch("pytube.cli.YouTube")
def test_download_when_itag_not_found(youtube, display_streams):
    # Given
    youtube.streams = mock.Mock()
    youtube.streams.get_by_itag.return_value = None
    # When
    with pytest.raises(SystemExit):
        cli.download_by_itag(youtube, 123)
    # Then
    youtube.streams.get_by_itag.assert_called_with(123)
    display_streams.assert_called_with(youtube)


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.Stream")
def test_download_when_itag_is_found(youtube, stream):
    stream.itag = 123
    stream.exists_at_path.return_value = False
    youtube.streams = StreamQuery([stream])
    with patch.object(
        youtube.streams, "get_by_itag", wraps=youtube.streams.get_by_itag
    ) as wrapped_itag:
        cli.download_by_itag(youtube, 123)
        wrapped_itag.assert_called_with(123)
    youtube.register_on_progress_callback.assert_called_with(cli.on_progress)
    stream.download.assert_called()


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.Stream")
def test_display_stream(youtube, stream):
    # Given
    stream.itag = 123
    stream.__repr__ = MagicMock(return_value="")
    youtube.streams = StreamQuery([stream])
    # When
    cli.display_streams(youtube)
    # Then
    stream.__repr__.assert_called()


@mock.patch("pytube.cli._print_available_captions")
@mock.patch("pytube.cli.YouTube")
def test_download_caption_with_none(youtube, print_available):
    # Given
    caption = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    youtube.captions = CaptionQuery([caption])
    # When
    cli.download_caption(youtube, None)
    # Then
    print_available.assert_called_with(youtube.captions)


@mock.patch("pytube.cli.YouTube")
def test_download_caption_with_language_found(youtube):
    youtube.title = "video title"
    caption = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    caption.download = MagicMock(return_value="file_path")
    youtube.captions = CaptionQuery([caption])
    cli.download_caption(youtube, "en")
    caption.download.assert_called_with(title="video title", output_path=None)


@mock.patch("pytube.cli._print_available_captions")
@mock.patch("pytube.cli.YouTube")
def test_download_caption_with_lang_not_found(youtube, print_available):
    # Given
    caption = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    youtube.captions = CaptionQuery([caption])
    # When
    cli.download_caption(youtube, "blah")
    # Then
    print_available.assert_called_with(youtube.captions)


def test_print_available_captions(capsys):
    # Given
    caption1 = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    caption2 = Caption(
        {"url": "url2", "name": {"simpleText": "name2"}, "languageCode": "fr", "vssId": ".fr"}
    )
    query = CaptionQuery([caption1, caption2])
    # When
    cli._print_available_captions(query)
    # Then
    captured = capsys.readouterr()
    assert captured.out == "Available caption codes are: en, fr\n"


def test_display_progress_bar(capsys):
    cli.display_progress_bar(bytes_received=25, filesize=100, scale=0.55)
    out, _ = capsys.readouterr()
    assert "25.0%" in out


@mock.patch("pytube.Stream")
def test_on_progress(stream):
    stream.filesize = 10
    cli.display_progress_bar = MagicMock()
    cli.on_progress(stream, "", 7)
    cli.display_progress_bar.assert_called_once_with(3, 10)


def test_parse_args_falsey():
    parser = argparse.ArgumentParser()
    args = cli._parse_args(parser, ["http://youtube.com/watch?v=9bZkp7q19f0"])
    assert args.url == "http://youtube.com/watch?v=9bZkp7q19f0"
    assert args.build_playback_report is False
    assert args.itag is None
    assert args.list is False
    assert args.verbose is False


def test_parse_args_truthy():
    parser = argparse.ArgumentParser()
    args = cli._parse_args(
        parser,
        [
            "http://youtube.com/watch?v=9bZkp7q19f0",
            "--build-playback-report",
            "-c",
            "en",
            "-l",
            "--itag=10",
            "-vvv",
        ],
    )
    assert args.url == "http://youtube.com/watch?v=9bZkp7q19f0"
    assert args.build_playback_report is True
    assert args.itag == 10
    assert args.list is True
    assert args.verbose is True


@mock.patch("pytube.cli.setup_logger", return_value=None)
def test_main_logging_setup(setup_logger):
    # Given
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["http://fakeurl", "-v"])
    cli._parse_args = MagicMock(return_value=args)
    # When
    with pytest.raises(SystemExit):
        cli.main()
    # Then
    setup_logger.assert_called_with(logging.DEBUG, log_filename=None)


@mock.patch("pytube.cli.YouTube", return_value=None)
def test_main_download_by_itag(youtube):
    parser = argparse.ArgumentParser()
    args = parse_args(
        parser, ["http://youtube.com/watch?v=9bZkp7q19f0", "--itag=10"]
    )
    cli._parse_args = MagicMock(return_value=args)
    cli.download_by_itag = MagicMock()
    cli.main()
    youtube.assert_called()
    cli.download_by_itag.assert_called()


@mock.patch("pytube.cli.YouTube", return_value=None)
def test_main_build_playback_report(youtube):
    parser = argparse.ArgumentParser()
    args = parse_args(
        parser,
        ["http://youtube.com/watch?v=9bZkp7q19f0", "--build-playback-report"],
    )
    cli._parse_args = MagicMock(return_value=args)
    cli.build_playback_report = MagicMock()
    cli.main()
    youtube.assert_called()
    cli.build_playback_report.assert_called()


@mock.patch("pytube.cli.YouTube", return_value=None)
def test_main_display_streams(youtube):
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["http://youtube.com/watch?v=9bZkp7q19f0", "-l"])
    cli._parse_args = MagicMock(return_value=args)
    cli.display_streams = MagicMock()
    cli.main()
    youtube.assert_called()
    cli.display_streams.assert_called()


@mock.patch("pytube.cli.YouTube", return_value=None)
def test_main_download_caption(youtube):
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["http://youtube.com/watch?v=9bZkp7q19f0", "-c", "en"])
    cli._parse_args = MagicMock(return_value=args)
    cli.download_caption = MagicMock()
    cli.main()
    youtube.assert_called()
    cli.download_caption.assert_called()


@mock.patch("pytube.cli.YouTube", return_value=None)
@mock.patch("pytube.cli.download_by_resolution")
def test_download_by_resolution_flag(youtube, download_by_resolution):
    parser = argparse.ArgumentParser()
    args = parse_args(
        parser, ["http://youtube.com/watch?v=9bZkp7q19f0", "-r", "320p"]
    )
    cli._parse_args = MagicMock(return_value=args)
    cli.main()
    youtube.assert_called()
    download_by_resolution.assert_called()


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli.Playlist")
@mock.patch("pytube.cli._perform_args_on_youtube")
def test_download_with_playlist(perform_args_on_youtube, playlist, youtube):
    # Given
    cli.safe_filename = MagicMock(return_value="safe_title")
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["https://www.youtube.com/playlist?list=PLyn"])
    cli._parse_args = MagicMock(return_value=args)
    videos = [youtube]
    playlist_instance = playlist.return_value
    playlist_instance.videos = videos
    # When
    cli.main()
    # Then
    playlist.assert_called()
    perform_args_on_youtube.assert_called_with(youtube, args)


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli.Playlist")
@mock.patch("pytube.cli._perform_args_on_youtube")
def test_download_with_playlist_video_error(
    perform_args_on_youtube, playlist, youtube, capsys
):
    # Given
    cli.safe_filename = MagicMock(return_value="safe_title")
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["https://www.youtube.com/playlist?list=PLyn"])
    cli._parse_args = MagicMock(return_value=args)
    videos = [youtube]
    playlist_instance = playlist.return_value
    playlist_instance.videos = videos
    perform_args_on_youtube.side_effect = PytubeError()
    # When
    cli.main()
    # Then
    playlist.assert_called()
    captured = capsys.readouterr()
    assert "There was an error with video" in captured.out


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.StreamQuery")
@mock.patch("pytube.Stream")
@mock.patch("pytube.cli._download")
def test_download_by_resolution(download, stream, stream_query, youtube):
    # Given
    stream_query.get_by_resolution.return_value = stream
    youtube.streams = stream_query
    # When
    cli.download_by_resolution(
        youtube=youtube, resolution="320p", target="test_target"
    )
    # Then
    download.assert_called_with(stream, target="test_target")


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.StreamQuery")
@mock.patch("pytube.cli._download")
def test_download_by_resolution_not_exists(download, stream_query, youtube):
    stream_query.get_by_resolution.return_value = None
    youtube.streams = stream_query
    with pytest.raises(SystemExit):
        cli.download_by_resolution(
            youtube=youtube, resolution="DOESNT EXIST", target="test_target"
        )
    download.assert_not_called()


@mock.patch("pytube.Stream")
def test_download_stream_file_exists(stream, capsys):
    # Given
    stream.exists_at_path.return_value = True
    # When
    cli._download(stream=stream)
    # Then
    captured = capsys.readouterr()
    assert "Already downloaded at" in captured.out
    stream.download.assert_not_called()


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli.ffmpeg_process")
def test_perform_args_should_ffmpeg_process(ffmpeg_process, youtube):
    # Given
    parser = argparse.ArgumentParser()
    args = parse_args(
        parser, ["http://youtube.com/watch?v=9bZkp7q19f0", "-f", "best"]
    )
    cli._parse_args = MagicMock(return_value=args)
    # When
    cli._perform_args_on_youtube(youtube, args)
    # Then
    ffmpeg_process.assert_called_with(
        youtube=youtube, resolution="best", target=None
    )


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli._ffmpeg_downloader")
def test_ffmpeg_process_best_should_download(  # noqa: PT019
    _ffmpeg_downloader, youtube
):
    # Given
    target = "/target"
    streams = MagicMock()
    youtube.streams = streams
    video_stream = MagicMock()
    streams.filter.return_value.order_by.return_value.last.return_value = (
        video_stream
    )
    audio_stream = MagicMock()
    streams.get_audio_only.return_value = audio_stream
    # When
    cli.ffmpeg_process(youtube, "best", target)
    # Then
    _ffmpeg_downloader.assert_called_with(
        audio_stream=audio_stream, video_stream=video_stream, target=target
    )


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli._ffmpeg_downloader")
def test_ffmpeg_process_res_should_download(  # noqa: PT019
    _ffmpeg_downloader, youtube
):
    # Given
    target = "/target"
    streams = MagicMock()
    youtube.streams = streams
    video_stream = MagicMock()
    streams.filter.return_value.first.return_value = video_stream
    audio_stream = MagicMock()
    streams.get_audio_only.return_value = audio_stream
    # When
    cli.ffmpeg_process(youtube, "XYZp", target)
    # Then
    _ffmpeg_downloader.assert_called_with(
        audio_stream=audio_stream, video_stream=video_stream, target=target
    )


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli._ffmpeg_downloader")
def test_ffmpeg_process_res_none_should_not_download(  # noqa: PT019
    _ffmpeg_downloader, youtube
):
    # Given
    target = "/target"
    streams = MagicMock()
    youtube.streams = streams
    streams.filter.return_value.first.return_value = None
    audio_stream = MagicMock()
    streams.get_audio_only.return_value = audio_stream
    # When
    with pytest.raises(SystemExit):
        cli.ffmpeg_process(youtube, "XYZp", target)
    # Then
    _ffmpeg_downloader.assert_not_called()


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli._ffmpeg_downloader")
def test_ffmpeg_process_audio_none_should_fallback_download(  # noqa: PT019
    _ffmpeg_downloader, youtube
):
    # Given
    target = "/target"
    streams = MagicMock()
    youtube.streams = streams
    stream = MagicMock()
    streams.filter.return_value.order_by.return_value.last.return_value = stream
    streams.get_audio_only.return_value = None
    # When
    cli.ffmpeg_process(youtube, "best", target)
    # Then
    _ffmpeg_downloader.assert_called_with(
        audio_stream=stream, video_stream=stream, target=target
    )


@mock.patch("pytube.cli.YouTube")
@mock.patch("pytube.cli._ffmpeg_downloader")
def test_ffmpeg_process_audio_fallback_none_should_exit(  # noqa: PT019
    _ffmpeg_downloader, youtube
):
    # Given
    target = "/target"
    streams = MagicMock()
    youtube.streams = streams
    stream = MagicMock()
    streams.filter.return_value.order_by.return_value.last.side_effect = [
        stream,
        stream,
        None,
    ]
    streams.get_audio_only.return_value = None
    # When
    with pytest.raises(SystemExit):
        cli.ffmpeg_process(youtube, "best", target)
    # Then
    _ffmpeg_downloader.assert_not_called()


@mock.patch("pytube.cli.os.unlink", return_value=None)
@mock.patch("pytube.cli.subprocess.run", return_value=None)
@mock.patch("pytube.cli._download", return_value=None)
@mock.patch("pytube.cli._unique_name", return_value=None)
def test_ffmpeg_downloader(unique_name, download, run, unlink):
    # Given
    target = "target"
    audio_stream = MagicMock()
    video_stream = MagicMock()
    video_stream.id = "video_id"
    audio_stream.subtype = "audio_subtype"
    video_stream.subtype = "video_subtype"
    unique_name.side_effect = ["video_name", "audio_name"]

    # When
    cli._ffmpeg_downloader(
        audio_stream=audio_stream, video_stream=video_stream, target=target
    )
    # Then
    download.assert_called()
    run.assert_called_with(
        [
            "ffmpeg",
            "-i",
            os.path.join("target", "video_name.video_subtype"),
            "-i",
            os.path.join("target", "audio_name.audio_subtype"),
            "-codec",
            "copy",
            os.path.join("target", "safe_title.video_subtype"),
        ]
    )
    unlink.assert_called()


@mock.patch("pytube.cli.download_audio")
@mock.patch("pytube.cli.YouTube.__init__", return_value=None)
def test_download_audio_args(youtube, download_audio):
    # Given
    parser = argparse.ArgumentParser()
    args = parse_args(
        parser, ["http://youtube.com/watch?v=9bZkp7q19f0", "-a", "mp4"]
    )
    cli._parse_args = MagicMock(return_value=args)
    # When
    cli.main()
    # Then
    youtube.assert_called()
    download_audio.assert_called()


@mock.patch("pytube.cli._download")
@mock.patch("pytube.cli.YouTube")
def test_download_audio(youtube, download):
    # Given
    youtube_instance = youtube.return_value
    audio_stream = MagicMock()
    youtube_instance.streams.filter.return_value.order_by.return_value.last.return_value = (
        audio_stream
    )
    # When
    cli.download_audio(youtube_instance, "filetype", "target")
    # Then
    download.assert_called_with(audio_stream, target="target")


@mock.patch("pytube.cli._download")
@mock.patch("pytube.cli.YouTube")
def test_download_audio_none(youtube, download):
    # Given
    youtube_instance = youtube.return_value
    youtube_instance.streams.filter.return_value.order_by.return_value.last.return_value = (
        None
    )
    # When
    with pytest.raises(SystemExit):
        cli.download_audio(youtube_instance, "filetype", "target")
    # Then
    download.assert_not_called()


@mock.patch("pytube.cli.YouTube.__init__", return_value=None)
def test_perform_args_on_youtube(youtube):
    parser = argparse.ArgumentParser()
    args = parse_args(parser, ["http://youtube.com/watch?v=9bZkp7q19f0"])
    cli._parse_args = MagicMock(return_value=args)
    cli._perform_args_on_youtube = MagicMock()
    cli.main()
    youtube.assert_called()
    cli._perform_args_on_youtube.assert_called()


@mock.patch("pytube.cli.os.path.exists", return_value=False)
def test_unique_name(path_exists):
    assert (
        cli._unique_name("base", "subtype", "video", "target") == "base_video_0"
    )


@mock.patch("pytube.cli.os.path.exists")
def test_unique_name_counter(path_exists):
    path_exists.side_effect = [True, False]
    assert (
        cli._unique_name("base", "subtype", "video", "target") == "base_video_1"
    )

```

# tests/test_itags.py
```python
from pytube import itags


def test_get_format_profile():
    profile = itags.get_format_profile(22)
    assert profile["resolution"] == "720p"


def test_get_format_profile_non_existant():
    profile = itags.get_format_profile(2239)
    assert profile["resolution"] is None

```

# tests/test_main.py
```python
from unittest import mock

import pytest

import pytube
from pytube import YouTube
from pytube.exceptions import RegexMatchError


@mock.patch("urllib.request.install_opener")
def test_install_proxy(opener):
    proxies = {"http": "http://www.example.com:3128/"}
    YouTube(
        "https://www.youtube.com/watch?v=9bZkp7q19f0",
        proxies=proxies,
    )
    opener.assert_called()


@mock.patch("pytube.request.get")
def test_video_unavailable(get):
    get.return_value = ""
    youtube = YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")
    with pytest.raises(RegexMatchError):
        youtube.check_availability()


def test_video_keywords(cipher_signature):
    expected = [
        'Rewind', 'Rewind 2019',
        'youtube rewind 2019', '#YouTubeRewind',
        'MrBeast', 'PewDiePie', 'James Charles',
        'Shane Dawson', 'CaseyNeistat', 'RiceGum',
        'Simone Giertz', 'JennaMarbles', 'Lilly Singh',
        'emma chamberlain', 'The Try Guys', 'Fortnite',
        'Minecraft', 'Roblox', 'Marshmello',
        'Garena Free Fire', 'GTA V', 'Lachlan',
        'Anaysa', 'jeffreestar', 'Noah Schnapp',
        'Jennelle Eliana', 'T-Series', 'Azzyland',
        'LazarBeam', 'Dude Perfect', 'David Dobrik',
        'KSI', 'NikkieTutorials', 'Kurzgesagt',
        'Jelly', 'Ariana Grande', 'Billie Eilish',
        'BLACKPINK', 'Year in Review'
    ]
    assert cipher_signature.keywords == expected


def test_js_caching(cipher_signature):
    assert pytube.__js__ is not None
    assert pytube.__js_url__ is not None
    assert pytube.__js__ == cipher_signature.js
    assert pytube.__js_url__ == cipher_signature.js_url


def test_channel_id(cipher_signature):
    assert cipher_signature.channel_id == 'UCBR8-60-B28hp2BmDPdntcQ'


def test_channel_url(cipher_signature):
    assert cipher_signature.channel_url == 'https://www.youtube.com/channel/UCBR8-60-B28hp2BmDPdntcQ'  # noqa:E501

```

# tests/test_cipher.py
```python
import pytest

from pytube import cipher
from pytube.exceptions import RegexMatchError


def test_map_functions():
    with pytest.raises(RegexMatchError):
        cipher.map_functions("asdf")


def test_get_initial_function_name_with_no_match_should_error():
    with pytest.raises(RegexMatchError):
        cipher.get_initial_function_name("asdf")


def test_get_transform_object_with_no_match_should_error():
    with pytest.raises(RegexMatchError):
        cipher.get_transform_object("asdf", var="lt")


def test_reverse():
    reversed_array = cipher.reverse([1, 2, 3, 4], None)
    assert reversed_array == [4, 3, 2, 1]


def test_splice():
    assert cipher.splice([1, 2, 3, 4], 2) == [3, 4]
    assert cipher.splice([1, 2, 3, 4], 1) == [2, 3, 4]


def test_throttling_reverse():
    a = [1, 2, 3, 4]
    cipher.throttling_reverse(a)
    assert a == [4, 3, 2, 1]


def test_throttling_push():
    a = [1, 2, 3, 4]
    cipher.throttling_push(a, 5)
    assert a == [1, 2, 3, 4, 5]


def test_throttling_unshift():
    a = [1, 2, 3, 4]
    cipher.throttling_unshift(a, 2)
    assert a == [3, 4, 1, 2]


def test_throttling_nested_splice():
    a = [1, 2, 3, 4]
    cipher.throttling_nested_splice(a, 2)
    assert a == [3, 2, 1, 4]
    cipher.throttling_nested_splice(a, 0)
    assert a == [3, 2, 1, 4]


def test_throttling_prepend():
    a = [1, 2, 3, 4]
    cipher.throttling_prepend(a, 1)
    assert a == [4, 1, 2, 3]
    a = [1, 2, 3, 4]
    cipher.throttling_prepend(a, 2)
    assert a == [3, 4, 1, 2]


def test_throttling_swap():
    a = [1, 2, 3, 4]
    cipher.throttling_swap(a, 3)
    assert a == [4, 2, 3, 1]


def test_js_splice():
    mapping = {

    }
    for args, result in mapping.items():
        a = [1, 2, 3, 4]
        assert cipher.js_splice(a, *args) == result


def test_get_throttling_function_name(base_js):
    base_js_code_fragments = [
        # Values expected as of 2022/02/04:
        {
            'raw_var' : r'var Apa=[hha]',
            'raw_code': r'a.url="";a.C&&(b=a.get("n"))&&(b=Apa[0](b),a.set("n",b),'\
                        r'Apa.length||hha(""))}};',
            'nfunc_name': 'hha'
        },
        # Values expected as of 2022/04/15:
        {
            'raw_var' : r'var $x=[uq]',
            'raw_code': r'a.url="";a.D&&(b=a.get("n"))&&(b=$x[0](b),a.set("n",b),'\
                        r'$x.length||uq(""))',
            'nfunc_name': 'uq'
        }
    ]
    for code_fragment, base_js_file in zip(base_js_code_fragments, base_js):
        assert code_fragment['raw_var'] in base_js_file
        assert code_fragment['raw_code'] in base_js_file
        func_name = cipher.get_throttling_function_name(base_js_file)
        assert func_name == code_fragment['nfunc_name']

```

# tests/test_streams.py
```python
import os
import random
import pytest
from datetime import datetime
from unittest import mock
from unittest.mock import MagicMock, Mock
from urllib.error import HTTPError

from pytube import request, Stream


@mock.patch("pytube.streams.request")
def test_stream_to_buffer(mock_request, cipher_signature):
    # Given
    stream_bytes = iter(
        [
            bytes(os.urandom(8 * 1024)),
            bytes(os.urandom(8 * 1024)),
            bytes(os.urandom(8 * 1024)),
        ]
    )
    mock_request.stream.return_value = stream_bytes
    buffer = MagicMock()
    # When
    cipher_signature.streams[0].stream_to_buffer(buffer)
    # Then
    assert buffer.write.call_count == 3


def test_filesize(cipher_signature):
    assert cipher_signature.streams[0].filesize == 3399554
    
def test_filesize_kb(cipher_signature):
    assert cipher_signature.streams[0].filesize_kb == float(3319.877)

def test_filesize_mb(cipher_signature):
    assert cipher_signature.streams[0].filesize_mb == float(3.243)

def test_filesize_gb(cipher_signature):
    assert cipher_signature.streams[0].filesize_gb == float(0.004)

def test_filesize_approx(cipher_signature):
    stream = cipher_signature.streams[0]

    assert stream.filesize_approx == 3403320
    stream.bitrate = None
    assert stream.filesize_approx == 3399554


def test_default_filename(cipher_signature):
    expected = "YouTube Rewind 2019 For the Record  YouTubeRewind.3gpp"
    stream = cipher_signature.streams[0]
    assert stream.default_filename == expected


def test_title(cipher_signature):
    expected = "YouTube Rewind 2019: For the Record | #YouTubeRewind"
    assert cipher_signature.title == expected


def test_expiration(cipher_signature):
    assert cipher_signature.streams[0].expiration >= datetime(2020, 10, 30, 5, 39, 41)


def test_caption_tracks(presigned_video):
    assert len(presigned_video.caption_tracks) == 13


def test_captions(presigned_video):
    assert len(presigned_video.captions) == 13


def test_description(cipher_signature):
    expected = (
        "In 2018, we made something you didn’t like. "
        "For Rewind 2019, let’s see what you DID like.\n\n"
        "Celebrating the creators, music and moments "
        "that mattered most to you in 2019. \n\n"
        "To learn how the top lists in Rewind were generated: "
        "https://rewind.youtube/about\n\n"
        "Top lists featured the following channels:\n\n"
        "@1MILLION Dance Studio \n@A4 \n@Anaysa \n"
        "@Andymation \n@Ariana Grande \n@Awez Darbar \n"
        "@AzzyLand \n@Billie Eilish \n@Black Gryph0n \n"
        "@BLACKPINK \n@ChapkisDanceUSA \n@Daddy Yankee \n"
        "@David Dobrik \n@Dude Perfect \n@Felipe Neto \n"
        "@Fischer's-フィッシャーズ- \n@Galen Hooks \n@ibighit \n"
        "@James Charles \n@jeffreestar \n@Jelly \n@Kylie Jenner \n"
        "@LazarBeam \n@Lil Dicky \n@Lil Nas X \n@LOUD \n@LOUD Babi \n"
        "@LOUD Coringa \n@Magnet World \n@MrBeast \n"
        "@Nilson Izaias Papinho Oficial \n@Noah Schnapp\n"
        "@백종원의 요리비책 Paik's Cuisine \n@Pencilmation \n@PewDiePie \n"
        "@SethEverman \n@shane \n@Shawn Mendes \n@Team Naach \n"
        "@whinderssonnunes \n@워크맨-Workman \n@하루한끼 one meal a day \n\n"
        "To see the full list of featured channels in Rewind 2019, "
        "visit: https://rewind.youtube/about"
    )
    assert cipher_signature.description == expected


def test_rating(cipher_signature):
    """Test the rating value of a YouTube object.

    This changes each time we rebuild the json files, so we want to use
    an estimate of where it will be. The two values seen to make this
    estimate were 2.073431 and 2.0860765. This represents a range of
    ~0.007 below and ~0.006 above 2.08. Allowing for up to 0.02 in either
    direction should provide a steady indicator of correctness.
    """
    assert abs(cipher_signature.rating - 2.08) < 0.02


def test_length(cipher_signature):
    assert cipher_signature.length == 337


def test_views(cipher_signature):
    assert cipher_signature.views >= 108531745


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "6796391"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
def test_download(cipher_signature):
    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        stream.download()


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "16384"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
@mock.patch("pytube.streams.target_directory", MagicMock(return_value="/target"))
def test_download_with_prefix(cipher_signature):
    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        file_path = stream.download(filename_prefix="prefix")
        assert file_path == os.path.join(
            "/target",
            "prefixYouTube Rewind 2019 For the Record  YouTubeRewind.3gpp"
        )


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "16384"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
@mock.patch("pytube.streams.target_directory", MagicMock(return_value="/target"))
def test_download_with_filename(cipher_signature):
    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        file_path = stream.download(filename="cool name bro")
        assert file_path == os.path.join(
            "/target",
            "cool name bro"
        )


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "16384"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
@mock.patch("pytube.streams.target_directory", MagicMock(return_value="/target"))
@mock.patch("os.path.isfile", MagicMock(return_value=True))
def test_download_with_existing(cipher_signature):
    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        os.path.getsize = Mock(return_value=stream.filesize)
        file_path = stream.download()
        assert file_path == os.path.join(
            "/target",
            "YouTube Rewind 2019 For the Record  YouTubeRewind.3gpp"
        )
        assert not request.stream.called


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "16384"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
@mock.patch("pytube.streams.target_directory", MagicMock(return_value="/target"))
@mock.patch("os.path.isfile", MagicMock(return_value=True))
def test_download_with_existing_no_skip(cipher_signature):
    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        os.path.getsize = Mock(return_value=stream.filesize)
        file_path = stream.download(skip_existing=False)
        assert file_path == os.path.join(
            "/target",
            "YouTube Rewind 2019 For the Record  YouTubeRewind.3gpp"
        )
        assert request.stream.called


def test_progressive_streams_return_includes_audio_track(cipher_signature):
    stream = cipher_signature.streams.filter(progressive=True)[0]
    assert stream.includes_audio_track


def test_progressive_streams_return_includes_video_track(cipher_signature):
    stream = cipher_signature.streams.filter(progressive=True)[0]
    assert stream.includes_video_track


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "16384"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
def test_on_progress_hook(cipher_signature):
    callback_fn = mock.MagicMock()
    cipher_signature.register_on_progress_callback(callback_fn)

    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        stream.download()
    assert callback_fn.called
    args, _ = callback_fn.call_args
    assert len(args) == 3
    stream, _, _ = args
    assert isinstance(stream, Stream)


@mock.patch(
    "pytube.request.head", MagicMock(return_value={"content-length": "16384"})
)
@mock.patch(
    "pytube.request.stream",
    MagicMock(return_value=iter([str(random.getrandbits(8 * 1024))])),
)
def test_on_complete_hook(cipher_signature):
    callback_fn = mock.MagicMock()
    cipher_signature.register_on_complete_callback(callback_fn)

    with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
        stream = cipher_signature.streams[0]
        stream.download()
    assert callback_fn.called


def test_author(cipher_signature):
    assert cipher_signature.author == 'YouTube'


def test_thumbnail_when_in_details(cipher_signature):
    expected = f"https://i.ytimg.com/vi/{cipher_signature.video_id}/sddefault.jpg"
    cipher_signature._player_response = {
        "videoDetails": {"thumbnail": {"thumbnails": [{"url": expected}]}}
    }
    assert cipher_signature.thumbnail_url == expected


def test_repr_for_audio_streams(cipher_signature):
    stream = str(cipher_signature.streams.filter(only_audio=True)[1])
    expected = (
        '<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" '
        'acodec="mp4a.40.2" progressive="False" type="audio">'
    )
    assert stream == expected


def test_repr_for_video_streams(cipher_signature):
    stream = str(cipher_signature.streams.filter(only_video=True)[0])
    expected = (
        '<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" '
        'vcodec="avc1.640028" progressive="False" type="video">'
    )
    assert stream == expected


def test_repr_for_progressive_streams(cipher_signature):
    stream_reprs = [
        str(s)
        for s in cipher_signature.streams.filter(progressive=True)
    ]
    expected = (
        '<Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" '
        'vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" '
        'type="video">'
    )
    assert expected in stream_reprs


def test_repr_for_adaptive_streams(cipher_signature):
    stream = str(cipher_signature.streams.filter(adaptive=True)[0])
    expected = (
        '<Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" '
        'vcodec="avc1.640028" progressive="False" type="video">'
    )
    assert stream == expected


def test_segmented_stream_on_404(cipher_signature):
    stream = cipher_signature.streams.filter(adaptive=True)[0]
    with mock.patch('pytube.request.head') as mock_head:
        with mock.patch('pytube.request.urlopen') as mock_url_open:
            # Mock the responses to YouTube
            mock_url_open_object = mock.Mock()

            # These are our 4 "segments" of a dash stream
            # The first explains how many pieces there are, and
            # the rest are those pieces
            responses = [
                b'Raw_data\r\nSegment-Count: 3',
                b'a',
                b'b',
                b'c',
            ]
            joined_responses = b''.join(responses)

            # We create response headers to match the segments
            response_headers = [
                {
                    'content-length': len(r),
                    'Content-Range': '0-%s/%s' % (str(len(r)), str(len(r)))
                }
                for r in responses
            ]

            # Request order for stream:
            #   1. get(url&sn=0)
            #   2. head(url&sn=[1,2,3])
            #   3. info(url) -> 404
            #   4. get(url&sn=0)
            #   5. get(url&sn=[1,2,3])

            # Handle filesize requests
            mock_head.side_effect = [
                HTTPError('', 404, 'Not Found', '', ''),
                *response_headers[1:],
            ]

            # Each response must be followed by None, to break iteration
            #  in the stream() function
            mock_url_open_object.read.side_effect = [
                responses[0], None,
                responses[1], None,
                responses[2], None,
                responses[3], None,
            ]

            # This handles the HEAD requests to get content-length
            mock_url_open_object.info.side_effect = [
                HTTPError('', 404, 'Not Found', '', ''),
                *response_headers
            ]

            mock_url_open.return_value = mock_url_open_object

            with mock.patch('builtins.open', new_callable=mock.mock_open) as mock_open:
                file_handle = mock_open.return_value.__enter__.return_value
                fp = stream.download()
                full_content = b''
                for call in file_handle.write.call_args_list:
                    args, kwargs = call
                    full_content += b''.join(args)

                assert full_content == joined_responses
                mock_open.assert_called_once_with(fp, 'wb')


def test_segmented_only_catches_404(cipher_signature):
    stream = cipher_signature.streams.filter(adaptive=True)[0]
    with mock.patch('pytube.request.stream') as mock_stream:
        mock_stream.side_effect = HTTPError('', 403, 'Forbidden', '', '')
        with mock.patch("pytube.streams.open", mock.mock_open(), create=True):
            with pytest.raises(HTTPError):
                stream.download()

```

# tests/test_metadata.py
```python
"""Unit tests for the :module:`metadata <metadata>` module."""
from pytube import extract


def test_extract_metadata_empty():
    ytmd = extract.metadata({})
    assert ytmd._raw_metadata == []


def test_metadata_from_initial_data(stream_dict):
    initial_data = extract.initial_data(stream_dict)
    ytmd = extract.metadata(initial_data)
    assert len(ytmd.raw_metadata) > 0
    assert 'contents' in ytmd.raw_metadata[0]
    assert len(ytmd.metadata) > 0
    assert 'Song' in ytmd.metadata[0]

```

# tests/test_helpers.py
```python
import gzip
import io
import json
import os
import pytest
from unittest import mock

from pytube import helpers
from pytube.exceptions import RegexMatchError
from pytube.helpers import cache, create_mock_html_json, deprecated, setup_logger
from pytube.helpers import target_directory, uniqueify


def test_regex_search_no_match():
    with pytest.raises(RegexMatchError):
        helpers.regex_search("^a$", "", group=0)


def test_regex_search():
    assert helpers.regex_search("^a$", "a", group=0) == "a"


def test_safe_filename():
    """Unsafe characters get stripped from generated filename"""
    assert helpers.safe_filename("abc1245$$") == "abc1245"
    assert helpers.safe_filename("abc##") == "abc"


@mock.patch("warnings.warn")
def test_deprecated(warn):
    @deprecated("oh no")
    def deprecated_function():
        return None

    deprecated_function()
    warn.assert_called_with(
        "Call to deprecated function deprecated_function (oh no).",
        category=DeprecationWarning,
        stacklevel=2,
    )


def test_cache():
    call_count = 0

    @cache
    def cached_func(stuff):
        nonlocal call_count
        call_count += 1
        return stuff

    cached_func("hi")
    cached_func("hi")
    cached_func("bye")
    cached_func("bye")

    assert call_count == 2


@mock.patch("os.path.isabs", return_value=False)
@mock.patch("os.getcwd", return_value="/cwd")
@mock.patch("os.makedirs")
def test_target_directory_with_relative_path(_, __, makedirs):  # noqa: PT019
    assert target_directory("test") == os.path.join("/cwd", "test")
    makedirs.assert_called()


@mock.patch("os.path.isabs", return_value=True)
@mock.patch("os.makedirs")
def test_target_directory_with_absolute_path(_, makedirs):  # noqa: PT019
    assert target_directory("/test") == "/test"
    makedirs.assert_called()


@mock.patch("os.getcwd", return_value="/cwd")
@mock.patch("os.makedirs")
def test_target_directory_with_no_path(_, makedirs):  # noqa: PT019
    assert target_directory() == "/cwd"
    makedirs.assert_called()


@mock.patch("pytube.helpers.logging")
def test_setup_logger(logging):
    # Given
    logger = logging.getLogger.return_value
    # When
    setup_logger(20)
    # Then
    logging.getLogger.assert_called_with("pytube")
    logger.addHandler.assert_called()
    logger.setLevel.assert_called_with(20)


@mock.patch('builtins.open', new_callable=mock.mock_open)
@mock.patch('pytube.request.urlopen')
def test_create_mock_html_json(mock_url_open, mock_open):
    video_id = '2lAe1cqCOXo'
    gzip_html_filename = 'yt-video-%s-html.json.gz' % video_id

    # Get the pytube directory in order to navigate to /tests/mocks
    pytube_dir_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir
        )
    )
    pytube_mocks_path = os.path.join(pytube_dir_path, 'tests', 'mocks')
    gzip_html_filepath = os.path.join(pytube_mocks_path, gzip_html_filename)

    # Mock the responses to YouTube
    mock_url_open_object = mock.Mock()

    # Order is:
    # 1. watch_html -- must have jsurl match
    # 2. embed html
    # 3. watch html
    # 4. raw vid info
    mock_url_open_object.read.side_effect = [
        (b'yt.setConfig({"PLAYER_CONFIG":{"args":[]}});ytInitialData = {};ytInitialPlayerResponse = {};'  # noqa: E501
         b'"jsUrl":"/s/player/13371337/player_ias.vflset/en_US/base.js"'),
        b'embed_html',
        b'watch_html',
        b'{\"responseContext\":{}}',
    ]
    mock_url_open.return_value = mock_url_open_object

    # Generate a json with sample html json
    result_data = create_mock_html_json(video_id)

    # Assert that a write was only made once
    mock_open.assert_called_once_with(gzip_html_filepath, 'wb')

    # The result data should look like this:
    gzip_file = io.BytesIO()
    with gzip.GzipFile(
        filename=gzip_html_filename,
        fileobj=gzip_file,
        mode='wb'
    ) as f:
        f.write(json.dumps(result_data).encode('utf-8'))
    gzip_data = gzip_file.getvalue()

    file_handle = mock_open.return_value.__enter__.return_value

    # For some reason, write gets called multiple times, so we have to
    #  concatenate all the write calls to get the full data before we compare
    #  it to the BytesIO object value.
    full_content = b''
    for call in file_handle.write.call_args_list:
        args, kwargs = call
        full_content += b''.join(args)

    # The file header includes time metadata, so *occasionally* a single
    #  byte will be off at the very beginning. In theory, this difference
    #  should only affect bytes 5-8 (or [4:8] because of zero-indexing),
    #  but I've excluded the 10-byte metadata header altogether from the
    #  check, just to be safe.
    # Source: https://en.wikipedia.org/wiki/Gzip#File_format
    assert gzip_data[10:] == full_content[10:]


def test_uniqueify():
    non_unique_list = [1, 2, 3, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    result = uniqueify(non_unique_list)
    assert result == expected

```

# tests/test_extract.py
```python
"""Unit tests for the :module:`extract <extract>` module."""
from datetime import datetime
import pytest
import re

from pytube import extract
from pytube.exceptions import RegexMatchError


def test_extract_video_id():
    url = "https://www.youtube.com/watch?v=2lAe1cqCOXo"
    video_id = extract.video_id(url)
    assert video_id == "2lAe1cqCOXo"


def test_info_url(age_restricted):
    video_info_url = extract.video_info_url_age_restricted(
        video_id="QRS8MkLhQmM", embed_html=age_restricted["embed_html"],
    )
    assert video_info_url.startswith('https://www.youtube.com/get_video_info')
    assert 'video_id=QRS8MkLhQmM' in video_info_url


def test_info_url_age_restricted(cipher_signature):
    video_info_url = extract.video_info_url(
        video_id=cipher_signature.video_id,
        watch_url=cipher_signature.watch_url,
    )
    assert video_info_url.startswith('https://www.youtube.com/get_video_info')
    assert 'video_id=2lAe1cqCOXo' in video_info_url


def test_js_url(cipher_signature):
    expected = (
        r"https://youtube.com/s/player/([\w\d]+)/player_ias.vflset/en_US/base.js"
    )
    result = extract.js_url(cipher_signature.watch_html)
    match = re.search(expected, result)
    assert match is not None


def test_age_restricted(age_restricted):
    assert extract.is_age_restricted(age_restricted["watch_html"])


def test_non_age_restricted(cipher_signature):
    assert not extract.is_age_restricted(cipher_signature.watch_html)


def test_is_private(private):
    assert extract.is_private(private['watch_html'])


def test_not_is_private(cipher_signature):
    assert not extract.is_private(cipher_signature.watch_html)


def test_recording_available(cipher_signature):
    assert extract.recording_available(cipher_signature.watch_html)


def test_publish_date(cipher_signature):
    expected = datetime(2019, 12, 5)
    assert cipher_signature.publish_date == expected
    assert extract.publish_date('') is None


def test_not_recording_available(missing_recording):
    assert not extract.recording_available(missing_recording['watch_html'])


def test_mime_type_codec():
    mime_type, mime_subtype = extract.mime_type_codec(
        'audio/webm; codecs="opus"'
    )
    assert mime_type == "audio/webm"
    assert mime_subtype == ["opus"]


def test_mime_type_codec_with_no_match_should_error():
    with pytest.raises(RegexMatchError):
        extract.mime_type_codec("audio/webm")


def test_get_ytplayer_config_with_no_match_should_error():
    with pytest.raises(RegexMatchError):
        extract.get_ytplayer_config("")


def test_get_ytplayer_js_with_no_match_should_error():
    with pytest.raises(RegexMatchError):
        extract.get_ytplayer_js("")


def test_initial_data_missing():
    with pytest.raises(RegexMatchError):
        extract.initial_data('')


def test_initial_data(stream_dict):
    initial_data = extract.initial_data(stream_dict)
    assert 'contents' in initial_data

```

# tests/test_query.py
```python
"""Unit tests for the :class:`StreamQuery <StreamQuery>` class."""
import pytest


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        ({"progressive": True}, [17, 18, 22]),
        ({"resolution": "720p"}, [22, 136, 247, 398]),
        ({"res": "720p"}, [22, 136, 247, 398]),
        ({"fps": 24, "resolution": "480p"}, [135, 244, 397]),
        ({"mime_type": "audio/mp4"}, [139, 140]),
        ({"type": "audio"}, [139, 140, 249, 250, 251]),
        ({"subtype": "3gpp"}, [17]),
        ({"abr": "128kbps"}, [140]),
        ({"bitrate": "128kbps"}, [140]),
        ({"audio_codec": "opus"}, [249, 250, 251]),
        ({"video_codec": "vp9"}, [248, 247, 244, 243, 242, 278]),
        ({"only_audio": True}, [139, 140, 249, 250, 251]),
        ({"only_video": True, "video_codec": "avc1.4d4015"}, [133]),
        ({"adaptive": True, "resolution": "1080p"}, [137, 248, 399]),
        ({"custom_filter_functions": [lambda s: s.itag == 18]}, [18]),
    ],
)
def test_filters(test_input, expected, cipher_signature):
    """Ensure filters produce the expected results."""
    result = [s.itag for s in cipher_signature.streams.filter(**test_input)]
    assert result == expected


@pytest.mark.parametrize("test_input", ["first", "last"])
def test_empty(test_input, cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.last` and
    :meth:`~pytube.StreamQuery.first` return None if the resultset is
    empty.
    """
    query = cipher_signature.streams.filter(video_codec="vp20")
    fn = getattr(query, test_input)
    assert fn() is None


def test_get_last(cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.last` returns the expected
    :class:`Stream <Stream>`.
    """
    assert cipher_signature.streams[-1].itag == 251


def test_get_first(cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.first` returns the expected
    :class:`Stream <Stream>`.
    """
    assert cipher_signature.streams.first().itag == cipher_signature.streams[0].itag


def test_order_by(cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.order_by` sorts the list of
    :class:`Stream <Stream>` instances in the expected order.
    """
    itags = [
        s.itag
        for s in cipher_signature.streams.filter(type="audio").order_by("itag")
    ]
    expected_itags = [
        s.itag
        for s in cipher_signature.streams.filter(type="audio")
    ]
    expected_itags.sort()

    assert itags == expected_itags


def test_order_by_descending(cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.desc` sorts the list of
    :class:`Stream <Stream>` instances in the reverse order.
    """
    # numerical values
    itags = [
        s.itag
        for s in cipher_signature.streams.filter(type="audio")
        .order_by("itag")
        .desc()
    ]
    expected_itags = [
        s.itag
        for s in cipher_signature.streams.filter(type="audio")
    ]
    expected_itags.sort(reverse=True)
    assert itags == expected_itags


def test_order_by_non_numerical(cipher_signature):
    mime_types = [
        s.mime_type
        for s in cipher_signature.streams.filter(res="360p")
        .order_by("mime_type")
        .desc()
    ]
    assert mime_types == ["video/webm", "video/mp4", "video/mp4", "video/mp4"]


def test_order_by_ascending(cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.desc` sorts the list of
    :class:`Stream <Stream>` instances in ascending order.
    """
    # numerical values
    itags = [
        s.itag
        for s in cipher_signature.streams.filter(type="audio")
        .order_by("itag")
        .asc()
    ]
    expected_itags = [
        s.itag
        for s in cipher_signature.streams.filter(type="audio")
    ]
    assert itags == expected_itags


def test_order_by_non_numerical_ascending(cipher_signature):
    mime_types = [
        s.mime_type
        for s in cipher_signature.streams.filter(res="360p")
        .order_by("mime_type")
        .asc()
    ]
    assert mime_types == ["video/mp4", "video/mp4", "video/mp4", "video/webm"]


def test_order_by_with_none_values(cipher_signature):
    abrs = [s.abr for s in cipher_signature.streams.order_by("abr").asc()]
    assert abrs == [
        "24kbps",
        "48kbps",
        "50kbps",
        "70kbps",
        "96kbps",
        "128kbps",
        "160kbps",
        "192kbps"
    ]


def test_get_by_itag(cipher_signature):
    """Ensure :meth:`~pytube.StreamQuery.get_by_itag` returns the expected
    :class:`Stream <Stream>`.
    """
    assert cipher_signature.streams.get_by_itag(18).itag == 18


def test_get_by_non_existent_itag(cipher_signature):
    assert not cipher_signature.streams.get_by_itag(22983)


def test_get_by_resolution(cipher_signature):
    assert cipher_signature.streams.get_by_resolution("360p").itag == 18


def test_get_lowest_resolution(cipher_signature):
    assert cipher_signature.streams.get_lowest_resolution().itag == 18


def test_get_highest_resolution(cipher_signature):
    assert cipher_signature.streams.get_highest_resolution().itag == 22


def test_filter_is_dash(cipher_signature):
    streams = cipher_signature.streams.filter(is_dash=False)
    itags = [s.itag for s in streams]
    assert itags == [17, 18, 22]


def test_get_audio_only(cipher_signature):
    assert cipher_signature.streams.get_audio_only().itag == 140


def test_get_audio_only_with_subtype(cipher_signature):
    assert cipher_signature.streams.get_audio_only(subtype="webm").itag == 251


def test_sequence(cipher_signature):
    assert len(cipher_signature.streams) == 26
    assert cipher_signature.streams[0] is not None


def test_otf(cipher_signature):
    non_otf = cipher_signature.streams.otf()
    assert len(non_otf) == 26

    otf = cipher_signature.streams.otf(True)
    assert len(otf) == 0


def test_repr(cipher_signature):
    assert repr(
        cipher_signature.streams.filter(
            progressive=True, subtype="mp4", resolution="360p"
        )
    ) == (
        '[<Stream: itag="18" mime_type="video/mp4" '
        'res="360p" fps="24fps" vcodec="avc1.42001E" '
        'acodec="mp4a.40.2" progressive="True" type="video">]'
    )

```

# tests/test_parser.py
```python
import json
import pytest

from pytube.exceptions import HTMLParseError
from pytube.parser import parse_for_object


def test_invalid_start():
    with pytest.raises(HTMLParseError):
        parse_for_object('test = {}', r'invalid_regex')


def test_parse_simple_empty_object():
    result = parse_for_object('test = {}', r'test\s*=\s*')
    assert result == {}


def test_parse_longer_empty_object():
    test_html = """test = {


    }"""
    result = parse_for_object(test_html, r'test\s*=\s*')
    assert result == {}


def test_parse_empty_object_with_trailing_characters():
    test_html = 'test = {};'
    result = parse_for_object(test_html, r'test\s*=\s*')
    assert result == {}


def test_parse_simple_object():
    test_html = 'test = {"foo": [], "bar": {}};'
    result = parse_for_object(test_html, r'test\s*=\s*')
    assert result == {
        'foo': [],
        'bar': {}
    }


def test_parse_context_closer_in_string_value():
    test_html = 'test = {"foo": "};"};'
    result = parse_for_object(test_html, r'test\s*=\s*')
    assert result == {
        'foo': '};'
    }


def test_parse_object_requiring_ast():
    invalid_json = '{"foo": "bar",}'
    test_html = f'test = {invalid_json}'
    with pytest.raises(json.decoder.JSONDecodeError):
        json.loads(invalid_json)
    result = parse_for_object(test_html, r'test\s*=\s*')
    assert result == {
        'foo': 'bar'
    }

```

# tests/test_captions.py
```python
import os
import pytest
from unittest import mock
from unittest.mock import MagicMock, mock_open, patch

from pytube import Caption, CaptionQuery, captions


def test_float_to_srt_time_format():
    caption1 = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    assert caption1.float_to_srt_time_format(3.89) == "00:00:03,890"


def test_caption_query_sequence():
    caption1 = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    caption2 = Caption(
        {"url": "url2", "name": {"simpleText": "name2"}, "languageCode": "fr", "vssId": ".fr"}
    )
    caption_query = CaptionQuery(captions=[caption1, caption2])
    assert len(caption_query) == 2
    assert caption_query["en"] == caption1
    assert caption_query["fr"] == caption2
    with pytest.raises(KeyError):
        assert caption_query["nada"] is not None


def test_caption_query_get_by_language_code_when_exists():
    caption1 = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    caption2 = Caption(
        {"url": "url2", "name": {"simpleText": "name2"}, "languageCode": "fr", "vssId": ".fr"}
    )
    caption_query = CaptionQuery(captions=[caption1, caption2])
    assert caption_query["en"] == caption1


def test_caption_query_get_by_language_code_when_not_exists():
    caption1 = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    caption2 = Caption(
        {"url": "url2", "name": {"simpleText": "name2"}, "languageCode": "fr", "vssId": ".fr"}
    )
    caption_query = CaptionQuery(captions=[caption1, caption2])
    with pytest.raises(KeyError):
        assert caption_query["hello"] is not None
        # assert not_found is not None  # should never reach here


@mock.patch("pytube.captions.Caption.generate_srt_captions")
def test_download(srt):
    open_mock = mock_open()
    with patch("builtins.open", open_mock):
        srt.return_value = ""
        caption = Caption(
            {
                "url": "url1",
                "name": {"simpleText": "name1"},
                "languageCode": "en",
                "vssId": ".en"
            }
        )
        caption.download("title")
        assert (
            open_mock.call_args_list[0][0][0].split(os.path.sep)[-1] == "title (en).srt"
        )


@mock.patch("pytube.captions.Caption.generate_srt_captions")
def test_download_with_prefix(srt):
    open_mock = mock_open()
    with patch("builtins.open", open_mock):
        srt.return_value = ""
        caption = Caption(
            {
                "url": "url1",
                "name": {"simpleText": "name1"},
                "languageCode": "en",
                "vssId": ".en"
            }
        )
        caption.download("title", filename_prefix="1 ")
        assert (
            open_mock.call_args_list[0][0][0].split(os.path.sep)[-1]
            == "1 title (en).srt"
        )


@mock.patch("pytube.captions.Caption.generate_srt_captions")
def test_download_with_output_path(srt):
    open_mock = mock_open()
    captions.target_directory = MagicMock(return_value="/target")
    with patch("builtins.open", open_mock):
        srt.return_value = ""
        caption = Caption(
            {
                "url": "url1",
                "name": {"simpleText": "name1"},
                "languageCode": "en",
                "vssId": ".en"
            }
        )
        file_path = caption.download("title", output_path="blah")
        assert file_path == os.path.join("/target","title (en).srt")
        captions.target_directory.assert_called_with("blah")


@mock.patch("pytube.captions.Caption.xml_captions")
def test_download_xml_and_trim_extension(xml):
    open_mock = mock_open()
    with patch("builtins.open", open_mock):
        xml.return_value = ""
        caption = Caption(
            {
                "url": "url1",
                "name": {"simpleText": "name1"},
                "languageCode": "en",
                "vssId": ".en"
            }
        )
        caption.download("title.xml", srt=False)
        assert (
            open_mock.call_args_list[0][0][0].split(os.path.sep)[-1] == "title (en).xml"
        )


def test_repr():
    caption = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    assert str(caption) == '<Caption lang="name1" code="en">'

    caption_query = CaptionQuery(captions=[caption])
    assert repr(caption_query) == '{\'en\': <Caption lang="name1" code="en">}'


@mock.patch("pytube.request.get")
def test_xml_captions(request_get):
    request_get.return_value = "test"
    caption = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    assert caption.xml_captions == "test"


@mock.patch("pytube.captions.request")
def test_generate_srt_captions(request):
    request.get.return_value = (
        '<?xml version="1.0" encoding="utf-8" ?><transcript><text start="6.5" dur="1.7">['
        'Herb, Software Engineer]\n本影片包含隱藏式字幕。</text><text start="8.3" dur="2.7">'
        "如要啓動字幕，請按一下這裡的圖示。</text></transcript>"
    )
    caption = Caption(
        {"url": "url1", "name": {"simpleText": "name1"}, "languageCode": "en", "vssId": ".en"}
    )
    assert caption.generate_srt_captions() == (
        "1\n"
        "00:00:06,500 --> 00:00:08,200\n"
        "[Herb, Software Engineer] 本影片包含隱藏式字幕。\n"
        "\n"
        "2\n"
        "00:00:08,300 --> 00:00:11,000\n"
        "如要啓動字幕，請按一下這裡的圖示。"
    )

```

# docs/requirements.txt
```plaintext
typing_extensions

```

# docs/conf.py
```python
#!/usr/bin/env python3
"""pytube documentation build configuration file."""
import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("../"))

from pytube import __version__  # noqa

# -- General configuration ------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md'] # noqa: E800
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "pytube"
author = "Ronnie Ghose, Taylor Fox Dahlin, Nick Ficano"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {} # noqa: E800

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",  # needs 'show_related': True theme option to display
        "searchbox.html",
        "donate.html",
    ],
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "pytubedoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "pytube.tex",
        "pytube Documentation",
        "Nick Ficano",
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "pytube", "pytube Documentation", [author], 1,),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "pytube",
        "pytube Documentation",
        author,
        "pytube",
        "One line description of project.",
        "Miscellaneous",
    ),
]

```

# pytube/monostate.py
```python
from typing import Any, Callable, Optional


class Monostate:
    def __init__(
        self,
        on_progress: Optional[Callable[[Any, bytes, int], None]],
        on_complete: Optional[Callable[[Any, Optional[str]], None]],
        title: Optional[str] = None,
        duration: Optional[int] = None,
    ):
        self.on_progress = on_progress
        self.on_complete = on_complete
        self.title = title
        self.duration = duration

```

# pytube/__init__.py
```python
# flake8: noqa: F401
# noreorder
"""
Pytube: a very serious Python library for downloading YouTube Videos.
"""
__title__ = "pytube"
__author__ = "Ronnie Ghose, Taylor Fox Dahlin, Nick Ficano"
__license__ = "The Unlicense (Unlicense)"
__js__ = None
__js_url__ = None

from pytube.version import __version__
from pytube.streams import Stream
from pytube.captions import Caption
from pytube.query import CaptionQuery, StreamQuery
from pytube.__main__ import YouTube
from pytube.contrib.playlist import Playlist
from pytube.contrib.channel import Channel
from pytube.contrib.search import Search

```

# pytube/version.py
```python
__version__ = "15.0.0"

if __name__ == "__main__":
    print(__version__)

```

# pytube/innertube.py
```python
"""This module is designed to interact with the innertube API.

This module is NOT intended to be used directly by end users, as each of the
interfaces returns raw results. These should instead be parsed to extract
the useful information for the end user.
"""
# Native python imports
import json
import os
import pathlib
import time
from urllib import parse

# Local imports
from pytube import request

# YouTube on TV client secrets
_client_id = '861556708454-d6dlm3lh05idd8npek18k6be8ba3oc68.apps.googleusercontent.com'
_client_secret = 'SboVhoG9s0rNafixCSGGKXAT'

# Extracted API keys -- unclear what these are linked to.
_api_keys = [
    'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    'AIzaSyCtkvNIR1HCEwzsqK6JuE6KqpyjusIRI30',
    'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
    'AIzaSyC8UYZpvA2eknNex0Pjid0_eTLJoDu6los',
    'AIzaSyCjc_pVEDi4qsv5MtC2dMXzpIaDoRFLsxw',
    'AIzaSyDHQ9ipnphqTzDqZsbtd8_Ru4_kiKVQe2k'
]

_default_clients = {
    'WEB': {
        'context': {
            'client': {
                'clientName': 'WEB',
                'clientVersion': '2.20200720.00.02'
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'ANDROID': {
        'context': {
            'client': {
                'clientName': 'ANDROID',
                'clientVersion': '17.31.35',
                'androidSdkVersion': 30
            }
        },
        'header': {
            'User-Agent': 'com.google.android.youtube/',
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'IOS': {
        'context': {
            'client': {
                'clientName': 'IOS',
                'clientVersion': '17.33.2',
                'deviceModel': 'iPhone14,3'
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.youtube/'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },

    'WEB_EMBED': {
        'context': {
            'client': {
                'clientName': 'WEB_EMBEDDED_PLAYER',
                'clientVersion': '2.20210721.00.00',
                'clientScreen': 'EMBED'
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'ANDROID_EMBED': {
        'context': {
            'client': {
                'clientName': 'ANDROID_EMBEDDED_PLAYER',
                'clientVersion': '17.31.35',
                'clientScreen': 'EMBED',
                'androidSdkVersion': 30,
            }
        },
        'header': {
            'User-Agent': 'com.google.android.youtube/'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'IOS_EMBED': {
        'context': {
            'client': {
                'clientName': 'IOS_MESSAGES_EXTENSION',
                'clientVersion': '17.33.2',
                'deviceModel': 'iPhone14,3'
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.youtube/'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },

    'WEB_MUSIC': {
        'context': {
            'client': {
                'clientName': 'WEB_REMIX',
                'clientVersion': '1.20220727.01.00',
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'ANDROID_MUSIC': {
        'context': {
            'client': {
                'clientName': 'ANDROID_MUSIC',
                'clientVersion': '5.16.51',
                'androidSdkVersion': 30
            }
        },
        'header': {
            'User-Agent': 'com.google.android.apps.youtube.music/'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'IOS_MUSIC': {
        'context': {
            'client': {
                'clientName': 'IOS_MUSIC',
                'clientVersion': '5.21',
                'deviceModel': 'iPhone14,3'
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.youtubemusic/'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },

    'WEB_CREATOR': {
        'context': {
            'client': {
                'clientName': 'WEB_CREATOR',
                'clientVersion': '1.20220726.00.00',
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'ANDROID_CREATOR': {
        'context': {
            'client': {
                'clientName': 'ANDROID_CREATOR',
                'clientVersion': '22.30.100',
                'androidSdkVersion': 30,
            }
        },
        'header': {
            'User-Agent': 'com.google.android.apps.youtube.creator/',
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
    'IOS_CREATOR': {
        'context': {
            'client': {
                'clientName': 'IOS_CREATOR',
                'clientVersion': '22.33.101',
                'deviceModel': 'iPhone14,3',
            }
        },
        'header': {
            'User-Agent': 'com.google.ios.ytcreator/'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },

    'MWEB': {
        'context': {
            'client': {
                'clientName': 'MWEB',
                'clientVersion': '2.20220801.00.00',
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },

    'TV_EMBED': {
        'context': {
            'client': {
                'clientName': 'TVHTML5_SIMPLY_EMBEDDED_PLAYER',
                'clientVersion': '2.0',
            }
        },
        'header': {
            'User-Agent': 'Mozilla/5.0'
        },
        'api_key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'
    },
}
_token_timeout = 1800
_cache_dir = pathlib.Path(__file__).parent.resolve() / '__cache__'
_token_file = os.path.join(_cache_dir, 'tokens.json')


class InnerTube:
    """Object for interacting with the innertube API."""
    def __init__(self, client='ANDROID_MUSIC', use_oauth=False, allow_cache=True):
        """Initialize an InnerTube object.

        :param str client:
            Client to use for the object.
            Default to web because it returns the most playback types.
        :param bool use_oauth:
            Whether or not to authenticate to YouTube.
        :param bool allow_cache:
            Allows caching of oauth tokens on the machine.
        """
        self.context = _default_clients[client]['context']
        self.header = _default_clients[client]['header']
        self.api_key = _default_clients[client]['api_key']
        self.access_token = None
        self.refresh_token = None
        self.use_oauth = use_oauth
        self.allow_cache = allow_cache

        # Stored as epoch time
        self.expires = None

        # Try to load from file if specified
        if self.use_oauth and self.allow_cache:
            # Try to load from file if possible
            if os.path.exists(_token_file):
                with open(_token_file) as f:
                    data = json.load(f)
                    self.access_token = data['access_token']
                    self.refresh_token = data['refresh_token']
                    self.expires = data['expires']
                    self.refresh_bearer_token()

    def cache_tokens(self):
        """Cache tokens to file if allowed."""
        if not self.allow_cache:
            return

        data = {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires': self.expires
        }
        if not os.path.exists(_cache_dir):
            os.mkdir(_cache_dir)
        with open(_token_file, 'w') as f:
            json.dump(data, f)

    def refresh_bearer_token(self, force=False):
        """Refreshes the OAuth token if necessary.

        :param bool force:
            Force-refresh the bearer token.
        """
        if not self.use_oauth:
            return
        # Skip refresh if it's not necessary and not forced
        if self.expires > time.time() and not force:
            return

        # Subtracting 30 seconds is arbitrary to avoid potential time discrepencies
        start_time = int(time.time() - 30)
        data = {
            'client_id': _client_id,
            'client_secret': _client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        response = request._execute_request(
            'https://oauth2.googleapis.com/token',
            'POST',
            headers={
                'Content-Type': 'application/json'
            },
            data=data
        )
        response_data = json.loads(response.read())

        self.access_token = response_data['access_token']
        self.expires = start_time + response_data['expires_in']
        self.cache_tokens()

    def fetch_bearer_token(self):
        """Fetch an OAuth token."""
        # Subtracting 30 seconds is arbitrary to avoid potential time discrepencies
        start_time = int(time.time() - 30)
        data = {
            'client_id': _client_id,
            'scope': 'https://www.googleapis.com/auth/youtube'
        }
        response = request._execute_request(
            'https://oauth2.googleapis.com/device/code',
            'POST',
            headers={
                'Content-Type': 'application/json'
            },
            data=data
        )
        response_data = json.loads(response.read())
        verification_url = response_data['verification_url']
        user_code = response_data['user_code']
        print(f'Please open {verification_url} and input code {user_code}')
        input('Press enter when you have completed this step.')

        data = {
            'client_id': _client_id,
            'client_secret': _client_secret,
            'device_code': response_data['device_code'],
            'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'
        }
        response = request._execute_request(
            'https://oauth2.googleapis.com/token',
            'POST',
            headers={
                'Content-Type': 'application/json'
            },
            data=data
        )
        response_data = json.loads(response.read())

        self.access_token = response_data['access_token']
        self.refresh_token = response_data['refresh_token']
        self.expires = start_time + response_data['expires_in']
        self.cache_tokens()

    @property
    def base_url(self):
        """Return the base url endpoint for the innertube API."""
        return 'https://www.youtube.com/youtubei/v1'

    @property
    def base_data(self):
        """Return the base json data to transmit to the innertube API."""
        return {
            'context': self.context
        }

    @property
    def base_params(self):
        """Return the base query parameters to transmit to the innertube API."""
        return {
            'key': self.api_key,
            'contentCheckOk': True,
            'racyCheckOk': True
        }

    def _call_api(self, endpoint, query, data):
        """Make a request to a given endpoint with the provided query parameters and data."""
        # Remove the API key if oauth is being used.
        if self.use_oauth:
            del query['key']

        endpoint_url = f'{endpoint}?{parse.urlencode(query)}'
        headers = {
            'Content-Type': 'application/json',
        }
        # Add the bearer token if applicable
        if self.use_oauth:
            if self.access_token:
                self.refresh_bearer_token()
                headers['Authorization'] = f'Bearer {self.access_token}'
            else:
                self.fetch_bearer_token()
                headers['Authorization'] = f'Bearer {self.access_token}'

        headers.update(self.header)

        response = request._execute_request(
            endpoint_url,
            'POST',
            headers=headers,
            data=data
        )
        return json.loads(response.read())

    def browse(self):
        """Make a request to the browse endpoint.

        TODO: Figure out how we can use this
        """
        # endpoint = f'{self.base_url}/browse'  # noqa:E800
        ...
        # return self._call_api(endpoint, query, self.base_data)  # noqa:E800

    def config(self):
        """Make a request to the config endpoint.

        TODO: Figure out how we can use this
        """
        # endpoint = f'{self.base_url}/config'  # noqa:E800
        ...
        # return self._call_api(endpoint, query, self.base_data)  # noqa:E800

    def guide(self):
        """Make a request to the guide endpoint.

        TODO: Figure out how we can use this
        """
        # endpoint = f'{self.base_url}/guide'  # noqa:E800
        ...
        # return self._call_api(endpoint, query, self.base_data)  # noqa:E800

    def next(self):
        """Make a request to the next endpoint.

        TODO: Figure out how we can use this
        """
        # endpoint = f'{self.base_url}/next'  # noqa:E800
        ...
        # return self._call_api(endpoint, query, self.base_data)  # noqa:E800

    def player(self, video_id):
        """Make a request to the player endpoint.

        :param str video_id:
            The video id to get player info for.
        :rtype: dict
        :returns:
            Raw player info results.
        """
        endpoint = f'{self.base_url}/player'
        query = {
            'videoId': video_id,
        }
        query.update(self.base_params)
        return self._call_api(endpoint, query, self.base_data)

    def search(self, search_query, continuation=None):
        """Make a request to the search endpoint.

        :param str search_query:
            The query to search.
        :rtype: dict
        :returns:
            Raw search query results.
        """
        endpoint = f'{self.base_url}/search'
        query = {
            'query': search_query
        }
        query.update(self.base_params)
        data = {}
        if continuation:
            data['continuation'] = continuation
        data.update(self.base_data)
        return self._call_api(endpoint, query, data)

    def verify_age(self, video_id):
        """Make a request to the age_verify endpoint.

        Notable examples of the types of video this verification step is for:
        * https://www.youtube.com/watch?v=QLdAhwSBZ3w
        * https://www.youtube.com/watch?v=hc0ZDaAZQT0

        :param str video_id:
            The video id to get player info for.
        :rtype: dict
        :returns:
            Returns information that includes a URL for bypassing certain restrictions.
        """
        endpoint = f'{self.base_url}/verify_age'
        data = {
            'nextEndpoint': {
                'urlEndpoint': {
                    'url': f'/watch?v={video_id}'
                }
            },
            'setControvercy': True
        }
        data.update(self.base_data)
        result = self._call_api(endpoint, self.base_params, data)
        return result

    def get_transcript(self, video_id):
        """Make a request to the get_transcript endpoint.

        This is likely related to captioning for videos, but is currently untested.
        """
        endpoint = f'{self.base_url}/get_transcript'
        query = {
            'videoId': video_id,
        }
        query.update(self.base_params)
        result = self._call_api(endpoint, query, self.base_data)
        return result

```

# pytube/captions.py
```python
import math
import os
import time
import json
import xml.etree.ElementTree as ElementTree
from html import unescape
from typing import Dict, Optional

from pytube import request
from pytube.helpers import safe_filename, target_directory


class Caption:
    """Container for caption tracks."""

    def __init__(self, caption_track: Dict):
        """Construct a :class:`Caption <Caption>`.

        :param dict caption_track:
            Caption track data extracted from ``watch_html``.
        """
        self.url = caption_track.get("baseUrl")

        # Certain videos have runs instead of simpleText
        #  this handles that edge case
        name_dict = caption_track['name']
        if 'simpleText' in name_dict:
            self.name = name_dict['simpleText']
        else:
            for el in name_dict['runs']:
                if 'text' in el:
                    self.name = el['text']

        # Use "vssId" instead of "languageCode", fix issue #779
        self.code = caption_track["vssId"]
        # Remove preceding '.' for backwards compatibility, e.g.:
        # English -> vssId: .en, languageCode: en
        # English (auto-generated) -> vssId: a.en, languageCode: en
        self.code = self.code.strip('.')

    @property
    def xml_captions(self) -> str:
        """Download the xml caption tracks."""
        return request.get(self.url)

    @property
    def json_captions(self) -> dict:
        """Download and parse the json caption tracks."""
        json_captions_url = self.url.replace('fmt=srv3','fmt=json3')
        text = request.get(json_captions_url)
        parsed = json.loads(text)
        assert parsed['wireMagic'] == 'pb3', 'Unexpected captions format'
        return parsed

    def generate_srt_captions(self) -> str:
        """Generate "SubRip Subtitle" captions.

        Takes the xml captions from :meth:`~pytube.Caption.xml_captions` and
        recompiles them into the "SubRip Subtitle" format.
        """
        return self.xml_caption_to_srt(self.xml_captions)

    @staticmethod
    def float_to_srt_time_format(d: float) -> str:
        """Convert decimal durations into proper srt format.

        :rtype: str
        :returns:
            SubRip Subtitle (str) formatted time duration.

        float_to_srt_time_format(3.89) -> '00:00:03,890'
        """
        fraction, whole = math.modf(d)
        time_fmt = time.strftime("%H:%M:%S,", time.gmtime(whole))
        ms = f"{fraction:.3f}".replace("0.", "")
        return time_fmt + ms

    def xml_caption_to_srt(self, xml_captions: str) -> str:
        """Convert xml caption tracks to "SubRip Subtitle (srt)".

        :param str xml_captions:
            XML formatted caption tracks.
        """
        segments = []
        root = ElementTree.fromstring(xml_captions)
        for i, child in enumerate(list(root)):
            text = child.text or ""
            caption = unescape(text.replace("\n", " ").replace("  ", " "),)
            try:
                duration = float(child.attrib["dur"])
            except KeyError:
                duration = 0.0
            start = float(child.attrib["start"])
            end = start + duration
            sequence_number = i + 1  # convert from 0-indexed to 1.
            line = "{seq}\n{start} --> {end}\n{text}\n".format(
                seq=sequence_number,
                start=self.float_to_srt_time_format(start),
                end=self.float_to_srt_time_format(end),
                text=caption,
            )
            segments.append(line)
        return "\n".join(segments).strip()

    def download(
        self,
        title: str,
        srt: bool = True,
        output_path: Optional[str] = None,
        filename_prefix: Optional[str] = None,
    ) -> str:
        """Write the media stream to disk.

        :param title:
            Output filename (stem only) for writing media file.
            If one is not specified, the default filename is used.
        :type title: str
        :param srt:
            Set to True to download srt, false to download xml. Defaults to True.
        :type srt bool
        :param output_path:
            (optional) Output path for writing media file. If one is not
            specified, defaults to the current working directory.
        :type output_path: str or None
        :param filename_prefix:
            (optional) A string that will be prepended to the filename.
            For example a number in a playlist or the name of a series.
            If one is not specified, nothing will be prepended
            This is separate from filename so you can use the default
            filename but still add a prefix.
        :type filename_prefix: str or None

        :rtype: str
        """
        if title.endswith(".srt") or title.endswith(".xml"):
            filename = ".".join(title.split(".")[:-1])
        else:
            filename = title

        if filename_prefix:
            filename = f"{safe_filename(filename_prefix)}{filename}"

        filename = safe_filename(filename)

        filename += f" ({self.code})"

        if srt:
            filename += ".srt"
        else:
            filename += ".xml"

        file_path = os.path.join(target_directory(output_path), filename)

        with open(file_path, "w", encoding="utf-8") as file_handle:
            if srt:
                file_handle.write(self.generate_srt_captions())
            else:
                file_handle.write(self.xml_captions)

        return file_path

    def __repr__(self):
        """Printable object representation."""
        return '<Caption lang="{s.name}" code="{s.code}">'.format(s=self)

```

# pytube/itags.py
```python
"""This module contains a lookup table of YouTube's itag values."""
from typing import Dict

PROGRESSIVE_VIDEO = {
    5: ("240p", "64kbps"),
    6: ("270p", "64kbps"),
    13: ("144p", None),
    17: ("144p", "24kbps"),
    18: ("360p", "96kbps"),
    22: ("720p", "192kbps"),
    34: ("360p", "128kbps"),
    35: ("480p", "128kbps"),
    36: ("240p", None),
    37: ("1080p", "192kbps"),
    38: ("3072p", "192kbps"),
    43: ("360p", "128kbps"),
    44: ("480p", "128kbps"),
    45: ("720p", "192kbps"),
    46: ("1080p", "192kbps"),
    59: ("480p", "128kbps"),
    78: ("480p", "128kbps"),
    82: ("360p", "128kbps"),
    83: ("480p", "128kbps"),
    84: ("720p", "192kbps"),
    85: ("1080p", "192kbps"),
    91: ("144p", "48kbps"),
    92: ("240p", "48kbps"),
    93: ("360p", "128kbps"),
    94: ("480p", "128kbps"),
    95: ("720p", "256kbps"),
    96: ("1080p", "256kbps"),
    100: ("360p", "128kbps"),
    101: ("480p", "192kbps"),
    102: ("720p", "192kbps"),
    132: ("240p", "48kbps"),
    151: ("720p", "24kbps"),
    300: ("720p", "128kbps"),
    301: ("1080p", "128kbps"),
}

DASH_VIDEO = {
    # DASH Video
    133: ("240p", None),  # MP4
    134: ("360p", None),  # MP4
    135: ("480p", None),  # MP4
    136: ("720p", None),  # MP4
    137: ("1080p", None),  # MP4
    138: ("2160p", None),  # MP4
    160: ("144p", None),  # MP4
    167: ("360p", None),  # WEBM
    168: ("480p", None),  # WEBM
    169: ("720p", None),  # WEBM
    170: ("1080p", None),  # WEBM
    212: ("480p", None),  # MP4
    218: ("480p", None),  # WEBM
    219: ("480p", None),  # WEBM
    242: ("240p", None),  # WEBM
    243: ("360p", None),  # WEBM
    244: ("480p", None),  # WEBM
    245: ("480p", None),  # WEBM
    246: ("480p", None),  # WEBM
    247: ("720p", None),  # WEBM
    248: ("1080p", None),  # WEBM
    264: ("1440p", None),  # MP4
    266: ("2160p", None),  # MP4
    271: ("1440p", None),  # WEBM
    272: ("4320p", None),  # WEBM
    278: ("144p", None),  # WEBM
    298: ("720p", None),  # MP4
    299: ("1080p", None),  # MP4
    302: ("720p", None),  # WEBM
    303: ("1080p", None),  # WEBM
    308: ("1440p", None),  # WEBM
    313: ("2160p", None),  # WEBM
    315: ("2160p", None),  # WEBM
    330: ("144p", None),  # WEBM
    331: ("240p", None),  # WEBM
    332: ("360p", None),  # WEBM
    333: ("480p", None),  # WEBM
    334: ("720p", None),  # WEBM
    335: ("1080p", None),  # WEBM
    336: ("1440p", None),  # WEBM
    337: ("2160p", None),  # WEBM
    394: ("144p", None),  # MP4
    395: ("240p", None),  # MP4
    396: ("360p", None),  # MP4
    397: ("480p", None),  # MP4
    398: ("720p", None),  # MP4
    399: ("1080p", None),  # MP4
    400: ("1440p", None),  # MP4
    401: ("2160p", None),  # MP4
    402: ("4320p", None),  # MP4
    571: ("4320p", None),  # MP4
    694: ("144p", None),  # MP4
    695: ("240p", None),  # MP4
    696: ("360p", None),  # MP4
    697: ("480p", None),  # MP4
    698: ("720p", None),  # MP4
    699: ("1080p", None),  # MP4
    700: ("1440p", None),  # MP4
    701: ("2160p", None),  # MP4
    702: ("4320p", None),  # MP4
}

DASH_AUDIO = {
    # DASH Audio
    139: (None, "48kbps"),  # MP4
    140: (None, "128kbps"),  # MP4
    141: (None, "256kbps"),  # MP4
    171: (None, "128kbps"),  # WEBM
    172: (None, "256kbps"),  # WEBM
    249: (None, "50kbps"),  # WEBM
    250: (None, "70kbps"),  # WEBM
    251: (None, "160kbps"),  # WEBM
    256: (None, "192kbps"),  # MP4
    258: (None, "384kbps"),  # MP4
    325: (None, None),  # MP4
    328: (None, None),  # MP4
}

ITAGS = {
    **PROGRESSIVE_VIDEO,
    **DASH_VIDEO,
    **DASH_AUDIO,
}

HDR = [330, 331, 332, 333, 334, 335, 336, 337]
_3D = [82, 83, 84, 85, 100, 101, 102]
LIVE = [91, 92, 93, 94, 95, 96, 132, 151]


def get_format_profile(itag: int) -> Dict:
    """Get additional format information for a given itag.

    :param str itag:
        YouTube format identifier code.
    """
    itag = int(itag)
    if itag in ITAGS:
        res, bitrate = ITAGS[itag]
    else:
        res, bitrate = None, None
    return {
        "resolution": res,
        "abr": bitrate,
        "is_live": itag in LIVE,
        "is_3d": itag in _3D,
        "is_hdr": itag in HDR,
        "is_dash": (
            itag in DASH_AUDIO
            or itag in DASH_VIDEO
        ),
    }

```

# pytube/request.py
```python
"""Implements a simple wrapper around urlopen."""
import http.client
import json
import logging
import re
import socket
from functools import lru_cache
from urllib import parse
from urllib.error import URLError
from urllib.request import Request, urlopen

from pytube.exceptions import RegexMatchError, MaxRetriesExceeded
from pytube.helpers import regex_search

logger = logging.getLogger(__name__)
default_range_size = 9437184  # 9MB


def _execute_request(
    url,
    method=None,
    headers=None,
    data=None,
    timeout=socket._GLOBAL_DEFAULT_TIMEOUT
):
    base_headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}
    if headers:
        base_headers.update(headers)
    if data:
        # encode data for request
        if not isinstance(data, bytes):
            data = bytes(json.dumps(data), encoding="utf-8")
    if url.lower().startswith("http"):
        request = Request(url, headers=base_headers, method=method, data=data)
    else:
        raise ValueError("Invalid URL")
    return urlopen(request, timeout=timeout)  # nosec


def get(url, extra_headers=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
    """Send an http GET request.

    :param str url:
        The URL to perform the GET request for.
    :param dict extra_headers:
        Extra headers to add to the request
    :rtype: str
    :returns:
        UTF-8 encoded string of response
    """
    if extra_headers is None:
        extra_headers = {}
    response = _execute_request(url, headers=extra_headers, timeout=timeout)
    return response.read().decode("utf-8")


def post(url, extra_headers=None, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
    """Send an http POST request.

    :param str url:
        The URL to perform the POST request for.
    :param dict extra_headers:
        Extra headers to add to the request
    :param dict data:
        The data to send on the POST request
    :rtype: str
    :returns:
        UTF-8 encoded string of response
    """
    # could technically be implemented in get,
    # but to avoid confusion implemented like this
    if extra_headers is None:
        extra_headers = {}
    if data is None:
        data = {}
    # required because the youtube servers are strict on content type
    # raises HTTPError [400]: Bad Request otherwise
    extra_headers.update({"Content-Type": "application/json"})
    response = _execute_request(
        url,
        headers=extra_headers,
        data=data,
        timeout=timeout
    )
    return response.read().decode("utf-8")


def seq_stream(
    url,
    timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
    max_retries=0
):
    """Read the response in sequence.
    :param str url: The URL to perform the GET request for.
    :rtype: Iterable[bytes]
    """
    # YouTube expects a request sequence number as part of the parameters.
    split_url = parse.urlsplit(url)
    base_url = '%s://%s/%s?' % (split_url.scheme, split_url.netloc, split_url.path)

    querys = dict(parse.parse_qsl(split_url.query))

    # The 0th sequential request provides the file headers, which tell us
    #  information about how the file is segmented.
    querys['sq'] = 0
    url = base_url + parse.urlencode(querys)

    segment_data = b''
    for chunk in stream(url, timeout=timeout, max_retries=max_retries):
        yield chunk
        segment_data += chunk

    # We can then parse the header to find the number of segments
    stream_info = segment_data.split(b'\r\n')
    segment_count_pattern = re.compile(b'Segment-Count: (\\d+)')
    for line in stream_info:
        match = segment_count_pattern.search(line)
        if match:
            segment_count = int(match.group(1).decode('utf-8'))

    # We request these segments sequentially to build the file.
    seq_num = 1
    while seq_num <= segment_count:
        # Create sequential request URL
        querys['sq'] = seq_num
        url = base_url + parse.urlencode(querys)

        yield from stream(url, timeout=timeout, max_retries=max_retries)
        seq_num += 1
    return  # pylint: disable=R1711


def stream(
    url,
    timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
    max_retries=0
):
    """Read the response in chunks.
    :param str url: The URL to perform the GET request for.
    :rtype: Iterable[bytes]
    """
    file_size: int = default_range_size  # fake filesize to start
    downloaded = 0
    while downloaded < file_size:
        stop_pos = min(downloaded + default_range_size, file_size) - 1
        range_header = f"bytes={downloaded}-{stop_pos}"
        tries = 0

        # Attempt to make the request multiple times as necessary.
        while True:
            # If the max retries is exceeded, raise an exception
            if tries >= 1 + max_retries:
                raise MaxRetriesExceeded()

            # Try to execute the request, ignoring socket timeouts
            try:
                response = _execute_request(
                    url + f"&range={downloaded}-{stop_pos}",
                    method="GET",
                    timeout=timeout
                )
            except URLError as e:
                # We only want to skip over timeout errors, and
                # raise any other URLError exceptions
                if isinstance(e.reason, socket.timeout):
                    pass
                else:
                    raise
            except http.client.IncompleteRead:
                # Allow retries on IncompleteRead errors for unreliable connections
                pass
            else:
                # On a successful request, break from loop
                break
            tries += 1

        if file_size == default_range_size:
            try:
                resp = _execute_request(
                    url + f"&range={0}-{99999999999}",
                    method="GET",
                    timeout=timeout
                )
                content_range = resp.info()["Content-Length"]
                file_size = int(content_range)
            except (KeyError, IndexError, ValueError) as e:
                logger.error(e)
        while True:
            chunk = response.read()
            if not chunk:
                break
            downloaded += len(chunk)
            yield chunk
    return  # pylint: disable=R1711


@lru_cache()
def filesize(url):
    """Fetch size in bytes of file at given URL

    :param str url: The URL to get the size of
    :returns: int: size in bytes of remote file
    """
    return int(head(url)["content-length"])


@lru_cache()
def seq_filesize(url):
    """Fetch size in bytes of file at given URL from sequential requests

    :param str url: The URL to get the size of
    :returns: int: size in bytes of remote file
    """
    total_filesize = 0
    # YouTube expects a request sequence number as part of the parameters.
    split_url = parse.urlsplit(url)
    base_url = '%s://%s/%s?' % (split_url.scheme, split_url.netloc, split_url.path)
    querys = dict(parse.parse_qsl(split_url.query))

    # The 0th sequential request provides the file headers, which tell us
    #  information about how the file is segmented.
    querys['sq'] = 0
    url = base_url + parse.urlencode(querys)
    response = _execute_request(
        url, method="GET"
    )

    response_value = response.read()
    # The file header must be added to the total filesize
    total_filesize += len(response_value)

    # We can then parse the header to find the number of segments
    segment_count = 0
    stream_info = response_value.split(b'\r\n')
    segment_regex = b'Segment-Count: (\\d+)'
    for line in stream_info:
        # One of the lines should contain the segment count, but we don't know
        #  which, so we need to iterate through the lines to find it
        try:
            segment_count = int(regex_search(segment_regex, line, 1))
        except RegexMatchError:
            pass

    if segment_count == 0:
        raise RegexMatchError('seq_filesize', segment_regex)

    # We make HEAD requests to the segments sequentially to find the total filesize.
    seq_num = 1
    while seq_num <= segment_count:
        # Create sequential request URL
        querys['sq'] = seq_num
        url = base_url + parse.urlencode(querys)

        total_filesize += int(head(url)['content-length'])
        seq_num += 1
    return total_filesize


def head(url):
    """Fetch headers returned http GET request.

    :param str url:
        The URL to perform the GET request for.
    :rtype: dict
    :returns:
        dictionary of lowercase headers
    """
    response_headers = _execute_request(url, method="HEAD").info()
    return {k.lower(): v for k, v in response_headers.items()}

```

# pytube/cli.py
```python
#!/usr/bin/env python3
"""A simple command line application to download youtube videos."""
import argparse
import gzip
import json
import logging
import os
import shutil
import sys
import datetime as dt
import subprocess  # nosec
from typing import List, Optional

import pytube.exceptions as exceptions
from pytube import __version__
from pytube import CaptionQuery, Playlist, Stream, YouTube
from pytube.helpers import safe_filename, setup_logger


logger = logging.getLogger(__name__)


def main():
    """Command line application to download youtube videos."""
    # noinspection PyTypeChecker
    parser = argparse.ArgumentParser(description=main.__doc__)
    args = _parse_args(parser)
    if args.verbose:
        log_filename = None
        if args.logfile:
            log_filename = args.logfile
        setup_logger(logging.DEBUG, log_filename=log_filename)
        logger.debug(f'Pytube version: {__version__}')

    if not args.url or "youtu" not in args.url:
        parser.print_help()
        sys.exit(1)

    if "/playlist" in args.url:
        print("Loading playlist...")
        playlist = Playlist(args.url)
        if not args.target:
            args.target = safe_filename(playlist.title)
        for youtube_video in playlist.videos:
            try:
                _perform_args_on_youtube(youtube_video, args)
            except exceptions.PytubeError as e:
                print(f"There was an error with video: {youtube_video}")
                print(e)
    else:
        print("Loading video...")
        youtube = YouTube(args.url)
        _perform_args_on_youtube(youtube, args)


def _perform_args_on_youtube(
    youtube: YouTube, args: argparse.Namespace
) -> None:
    if len(sys.argv) == 2 :  # no arguments parsed
        download_highest_resolution_progressive(
            youtube=youtube, resolution="highest", target=args.target
        )
    if args.list_captions:
        _print_available_captions(youtube.captions)
    if args.list:
        display_streams(youtube)
    if args.build_playback_report:
        build_playback_report(youtube)
    if args.itag:
        download_by_itag(youtube=youtube, itag=args.itag, target=args.target)
    if args.caption_code:
        download_caption(
            youtube=youtube, lang_code=args.caption_code, target=args.target
        )
    if args.resolution:
        download_by_resolution(
            youtube=youtube, resolution=args.resolution, target=args.target
        )
    if args.audio:
        download_audio(
            youtube=youtube, filetype=args.audio, target=args.target
        )
    if args.ffmpeg:
        ffmpeg_process(
            youtube=youtube, resolution=args.ffmpeg, target=args.target
        )


def _parse_args(
    parser: argparse.ArgumentParser, args: Optional[List] = None
) -> argparse.Namespace:
    parser.add_argument(
        "url", help="The YouTube /watch or /playlist url", nargs="?"
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__,
    )
    parser.add_argument(
        "--itag", type=int, help="The itag for the desired stream",
    )
    parser.add_argument(
        "-r",
        "--resolution",
        type=str,
        help="The resolution for the desired stream",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help=(
            "The list option causes pytube cli to return a list of streams "
            "available to download"
        ),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        help="Set logger output to verbose output.",
    )
    parser.add_argument(
        "--logfile",
        action="store",
        help="logging debug and error messages into a log file",
    )
    parser.add_argument(
        "--build-playback-report",
        action="store_true",
        help="Save the html and js to disk",
    )
    parser.add_argument(
        "-c",
        "--caption-code",
        type=str,
        help=(
            "Download srt captions for given language code. "
            "Prints available language codes if no argument given"
        ),
    )
    parser.add_argument(
        '-lc',
        '--list-captions',
        action='store_true',
        help=(
            "List available caption codes for a video"
        )
    )
    parser.add_argument(
        "-t",
        "--target",
        help=(
            "The output directory for the downloaded stream. "
            "Default is current working directory"
        ),
    )
    parser.add_argument(
        "-a",
        "--audio",
        const="mp4",
        nargs="?",
        help=(
            "Download the audio for a given URL at the highest bitrate available. "
            "Defaults to mp4 format if none is specified"
        ),
    )
    parser.add_argument(
        "-f",
        "--ffmpeg",
        const="best",
        nargs="?",
        help=(
            "Downloads the audio and video stream for resolution provided. "
            "If no resolution is provided, downloads the best resolution. "
            "Runs the command line program ffmpeg to combine the audio and video"
        ),
    )

    return parser.parse_args(args)


def build_playback_report(youtube: YouTube) -> None:
    """Serialize the request data to json for offline debugging.

    :param YouTube youtube:
        A YouTube object.
    """
    ts = int(dt.datetime.utcnow().timestamp())
    fp = os.path.join(os.getcwd(), f"yt-video-{youtube.video_id}-{ts}.json.gz")

    js = youtube.js
    watch_html = youtube.watch_html
    vid_info = youtube.vid_info

    with gzip.open(fp, "wb") as fh:
        fh.write(
            json.dumps(
                {
                    "url": youtube.watch_url,
                    "js": js,
                    "watch_html": watch_html,
                    "video_info": vid_info,
                }
            ).encode("utf8"),
        )


def display_progress_bar(
    bytes_received: int, filesize: int, ch: str = "█", scale: float = 0.55
) -> None:
    """Display a simple, pretty progress bar.

    Example:
    ~~~~~~~~
    PSY - GANGNAM STYLE(강남스타일) MV.mp4
    ↳ |███████████████████████████████████████| 100.0%

    :param int bytes_received:
        The delta between the total file size (bytes) and bytes already
        written to disk.
    :param int filesize:
        File size of the media stream in bytes.
    :param str ch:
        Character to use for presenting progress segment.
    :param float scale:
        Scale multiplier to reduce progress bar size.

    """
    columns = shutil.get_terminal_size().columns
    max_width = int(columns * scale)

    filled = int(round(max_width * bytes_received / float(filesize)))
    remaining = max_width - filled
    progress_bar = ch * filled + " " * remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = f" ↳ |{progress_bar}| {percent}%\r"
    sys.stdout.write(text)
    sys.stdout.flush()


# noinspection PyUnusedLocal
def on_progress(
    stream: Stream, chunk: bytes, bytes_remaining: int
) -> None:  # pylint: disable=W0613
    filesize = stream.filesize
    bytes_received = filesize - bytes_remaining
    display_progress_bar(bytes_received, filesize)


def _download(
    stream: Stream,
    target: Optional[str] = None,
    filename: Optional[str] = None,
) -> None:
    filesize_megabytes = stream.filesize // 1048576
    print(f"{filename or stream.default_filename} | {filesize_megabytes} MB")
    file_path = stream.get_file_path(filename=filename, output_path=target)
    if stream.exists_at_path(file_path):
        print(f"Already downloaded at:\n{file_path}")
        return

    stream.download(output_path=target, filename=filename)
    sys.stdout.write("\n")


def _unique_name(base: str, subtype: str, media_type: str, target: str) -> str:
    """
    Given a base name, the file format, and the target directory, will generate
    a filename unique for that directory and file format.
    :param str base:
        The given base-name.
    :param str subtype:
        The filetype of the video which will be downloaded.
    :param str media_type:
        The media_type of the file, ie. "audio" or "video"
    :param Path target:
        Target directory for download.
    """
    counter = 0
    while True:
        file_name = f"{base}_{media_type}_{counter}"
        file_path = os.path.join(target, f"{file_name}.{subtype}")
        if not os.path.exists(file_path):
            return file_name
        counter += 1


def ffmpeg_process(
    youtube: YouTube, resolution: str, target: Optional[str] = None
) -> None:
    """
    Decides the correct video stream to download, then calls _ffmpeg_downloader.

    :param YouTube youtube:
        A valid YouTube object.
    :param str resolution:
        YouTube video resolution.
    :param str target:
        Target directory for download
    """
    youtube.register_on_progress_callback(on_progress)
    target = target or os.getcwd()

    if resolution == "best":
        highest_quality_stream = (
            youtube.streams.filter(progressive=False)
            .order_by("resolution")
            .last()
        )
        mp4_stream = (
            youtube.streams.filter(progressive=False, subtype="mp4")
            .order_by("resolution")
            .last()
        )
        if highest_quality_stream.resolution == mp4_stream.resolution:
            video_stream = mp4_stream
        else:
            video_stream = highest_quality_stream
    else:
        video_stream = youtube.streams.filter(
            progressive=False, resolution=resolution, subtype="mp4"
        ).first()
        if not video_stream:
            video_stream = youtube.streams.filter(
                progressive=False, resolution=resolution
            ).first()
    if video_stream is None:
        print(f"Could not find a stream with resolution: {resolution}")
        print("Try one of these:")
        display_streams(youtube)
        sys.exit()

    audio_stream = youtube.streams.get_audio_only(video_stream.subtype)
    if not audio_stream:
        audio_stream = (
            youtube.streams.filter(only_audio=True).order_by("abr").last()
        )
    if not audio_stream:
        print("Could not find an audio only stream")
        sys.exit()
    _ffmpeg_downloader(
        audio_stream=audio_stream, video_stream=video_stream, target=target
    )


def _ffmpeg_downloader(
    audio_stream: Stream, video_stream: Stream, target: str
) -> None:
    """
    Given a YouTube Stream object, finds the correct audio stream, downloads them both
    giving them a unique name, them uses ffmpeg to create a new file with the audio
    and video from the previously downloaded files. Then deletes the original adaptive
    streams, leaving the combination.

    :param Stream audio_stream:
        A valid Stream object representing the audio to download
    :param Stream video_stream:
        A valid Stream object representing the video to download
    :param Path target:
        A valid Path object
    """
    video_unique_name = _unique_name(
        safe_filename(video_stream.title),
        video_stream.subtype,
        "video",
        target=target,
    )
    audio_unique_name = _unique_name(
        safe_filename(video_stream.title),
        audio_stream.subtype,
        "audio",
        target=target,
    )
    _download(stream=video_stream, target=target, filename=video_unique_name)
    print("Loading audio...")
    _download(stream=audio_stream, target=target, filename=audio_unique_name)

    video_path = os.path.join(
        target, f"{video_unique_name}.{video_stream.subtype}"
    )
    audio_path = os.path.join(
        target, f"{audio_unique_name}.{audio_stream.subtype}"
    )
    final_path = os.path.join(
        target, f"{safe_filename(video_stream.title)}.{video_stream.subtype}"
    )

    subprocess.run(  # nosec
        [
            "ffmpeg",
            "-i",
            video_path,
            "-i",
            audio_path,
            "-codec",
            "copy",
            final_path,
        ]
    )
    os.unlink(video_path)
    os.unlink(audio_path)


def download_by_itag(
    youtube: YouTube, itag: int, target: Optional[str] = None
) -> None:
    """Start downloading a YouTube video.

    :param YouTube youtube:
        A valid YouTube object.
    :param int itag:
        YouTube format identifier code.
    :param str target:
        Target directory for download
    """
    stream = youtube.streams.get_by_itag(itag)
    if stream is None:
        print(f"Could not find a stream with itag: {itag}")
        print("Try one of these:")
        display_streams(youtube)
        sys.exit()

    youtube.register_on_progress_callback(on_progress)

    try:
        _download(stream, target=target)
    except KeyboardInterrupt:
        sys.exit()


def download_by_resolution(
    youtube: YouTube, resolution: str, target: Optional[str] = None
) -> None:
    """Start downloading a YouTube video.

    :param YouTube youtube:
        A valid YouTube object.
    :param str resolution:
        YouTube video resolution.
    :param str target:
        Target directory for download
    """
    # TODO(nficano): allow dash itags to be selected
    stream = youtube.streams.get_by_resolution(resolution)
    if stream is None:
        print(f"Could not find a stream with resolution: {resolution}")
        print("Try one of these:")
        display_streams(youtube)
        sys.exit()

    youtube.register_on_progress_callback(on_progress)

    try:
        _download(stream, target=target)
    except KeyboardInterrupt:
        sys.exit()


def download_highest_resolution_progressive(
    youtube: YouTube, resolution: str, target: Optional[str] = None
) -> None:
    """Start downloading the highest resolution progressive stream.

    :param YouTube youtube:
        A valid YouTube object.
    :param str resolution:
        YouTube video resolution.
    :param str target:
        Target directory for download
    """
    youtube.register_on_progress_callback(on_progress)
    try:
        stream = youtube.streams.get_highest_resolution()
    except exceptions.VideoUnavailable as err:
        print(f"No video streams available: {err}")
    else:
        try:
            _download(stream, target=target)
        except KeyboardInterrupt:
            sys.exit()


def display_streams(youtube: YouTube) -> None:
    """Probe YouTube video and lists its available formats.

    :param YouTube youtube:
        A valid YouTube watch URL.

    """
    for stream in youtube.streams:
        print(stream)


def _print_available_captions(captions: CaptionQuery) -> None:
    print(
        f"Available caption codes are: {', '.join(c.code for c in captions)}"
    )


def download_caption(
    youtube: YouTube, lang_code: Optional[str], target: Optional[str] = None
) -> None:
    """Download a caption for the YouTube video.

    :param YouTube youtube:
        A valid YouTube object.
    :param str lang_code:
        Language code desired for caption file.
        Prints available codes if the value is None
        or the desired code is not available.
    :param str target:
        Target directory for download
    """
    try:
        caption = youtube.captions[lang_code]
        downloaded_path = caption.download(
            title=youtube.title, output_path=target
        )
        print(f"Saved caption file to: {downloaded_path}")
    except KeyError:
        print(f"Unable to find caption with code: {lang_code}")
        _print_available_captions(youtube.captions)


def download_audio(
    youtube: YouTube, filetype: str, target: Optional[str] = None
) -> None:
    """
    Given a filetype, downloads the highest quality available audio stream for a
    YouTube video.

    :param YouTube youtube:
        A valid YouTube object.
    :param str filetype:
        Desired file format to download.
    :param str target:
        Target directory for download
    """
    audio = (
        youtube.streams.filter(only_audio=True, subtype=filetype)
        .order_by("abr")
        .last()
    )

    if audio is None:
        print("No audio only stream found. Try one of these:")
        display_streams(youtube)
        sys.exit()

    youtube.register_on_progress_callback(on_progress)

    try:
        _download(audio, target=target)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()

```

# pytube/__main__.py
```python
"""
This module implements the core developer interface for pytube.

The problem domain of the :class:`YouTube <YouTube> class focuses almost
exclusively on the developer interface. Pytube offloads the heavy lifting to
smaller peripheral modules and functions.

"""
import logging
from typing import Any, Callable, Dict, List, Optional

import pytube
import pytube.exceptions as exceptions
from pytube import extract, request
from pytube import Stream, StreamQuery
from pytube.helpers import install_proxy
from pytube.innertube import InnerTube
from pytube.metadata import YouTubeMetadata
from pytube.monostate import Monostate

logger = logging.getLogger(__name__)


class YouTube:
    """Core developer interface for pytube."""

    def __init__(
        self,
        url: str,
        on_progress_callback: Optional[Callable[[Any, bytes, int], None]] = None,
        on_complete_callback: Optional[Callable[[Any, Optional[str]], None]] = None,
        proxies: Dict[str, str] = None,
        use_oauth: bool = False,
        allow_oauth_cache: bool = True
    ):
        """Construct a :class:`YouTube <YouTube>`.

        :param str url:
            A valid YouTube watch URL.
        :param func on_progress_callback:
            (Optional) User defined callback function for stream download
            progress events.
        :param func on_complete_callback:
            (Optional) User defined callback function for stream download
            complete events.
        :param dict proxies:
            (Optional) A dict mapping protocol to proxy address which will be used by pytube.
        :param bool use_oauth:
            (Optional) Prompt the user to authenticate to YouTube.
            If allow_oauth_cache is set to True, the user should only be prompted once.
        :param bool allow_oauth_cache:
            (Optional) Cache OAuth tokens locally on the machine. Defaults to True.
            These tokens are only generated if use_oauth is set to True as well.
        """
        self._js: Optional[str] = None  # js fetched by js_url
        self._js_url: Optional[str] = None  # the url to the js, parsed from watch html

        self._vid_info: Optional[Dict] = None  # content fetched from innertube/player

        self._watch_html: Optional[str] = None  # the html of /watch?v=<video_id>
        self._embed_html: Optional[str] = None
        self._player_config_args: Optional[Dict] = None  # inline js in the html containing
        self._age_restricted: Optional[bool] = None

        self._fmt_streams: Optional[List[Stream]] = None

        self._initial_data = None
        self._metadata: Optional[YouTubeMetadata] = None

        # video_id part of /watch?v=<video_id>
        self.video_id = extract.video_id(url)

        self.watch_url = f"https://youtube.com/watch?v={self.video_id}"
        self.embed_url = f"https://www.youtube.com/embed/{self.video_id}"

        # Shared between all instances of `Stream` (Borg pattern).
        self.stream_monostate = Monostate(
            on_progress=on_progress_callback, on_complete=on_complete_callback
        )

        if proxies:
            install_proxy(proxies)

        self._author = None
        self._title = None
        self._publish_date = None

        self.use_oauth = use_oauth
        self.allow_oauth_cache = allow_oauth_cache

    def __repr__(self):
        return f'<pytube.__main__.YouTube object: videoId={self.video_id}>'

    def __eq__(self, o: object) -> bool:
        # Compare types and urls, if they're same return true, else return false.
        return type(o) == type(self) and o.watch_url == self.watch_url

    @property
    def watch_html(self):
        if self._watch_html:
            return self._watch_html
        self._watch_html = request.get(url=self.watch_url)
        return self._watch_html

    @property
    def embed_html(self):
        if self._embed_html:
            return self._embed_html
        self._embed_html = request.get(url=self.embed_url)
        return self._embed_html

    @property
    def age_restricted(self):
        if self._age_restricted:
            return self._age_restricted
        self._age_restricted = extract.is_age_restricted(self.watch_html)
        return self._age_restricted

    @property
    def js_url(self):
        if self._js_url:
            return self._js_url

        if self.age_restricted:
            self._js_url = extract.js_url(self.embed_html)
        else:
            self._js_url = extract.js_url(self.watch_html)

        return self._js_url

    @property
    def js(self):
        if self._js:
            return self._js

        # If the js_url doesn't match the cached url, fetch the new js and update
        #  the cache; otherwise, load the cache.
        if pytube.__js_url__ != self.js_url:
            self._js = request.get(self.js_url)
            pytube.__js__ = self._js
            pytube.__js_url__ = self.js_url
        else:
            self._js = pytube.__js__

        return self._js

    @property
    def initial_data(self):
        if self._initial_data:
            return self._initial_data
        self._initial_data = extract.initial_data(self.watch_html)
        return self._initial_data

    @property
    def streaming_data(self):
        """Return streamingData from video info."""
        if 'streamingData' in self.vid_info:
            return self.vid_info['streamingData']
        else:
            self.bypass_age_gate()
            return self.vid_info['streamingData']

    @property
    def fmt_streams(self):
        """Returns a list of streams if they have been initialized.

        If the streams have not been initialized, finds all relevant
        streams and initializes them.
        """
        self.check_availability()
        if self._fmt_streams:
            return self._fmt_streams

        self._fmt_streams = []

        stream_manifest = extract.apply_descrambler(self.streaming_data)

        # If the cached js doesn't work, try fetching a new js file
        # https://github.com/pytube/pytube/issues/1054
        try:
            extract.apply_signature(stream_manifest, self.vid_info, self.js)
        except exceptions.ExtractError:
            # To force an update to the js file, we clear the cache and retry
            self._js = None
            self._js_url = None
            pytube.__js__ = None
            pytube.__js_url__ = None
            extract.apply_signature(stream_manifest, self.vid_info, self.js)

        # build instances of :class:`Stream <Stream>`
        # Initialize stream objects
        for stream in stream_manifest:
            video = Stream(
                stream=stream,
                monostate=self.stream_monostate,
            )
            self._fmt_streams.append(video)

        self.stream_monostate.title = self.title
        self.stream_monostate.duration = self.length

        return self._fmt_streams

    def check_availability(self):
        """Check whether the video is available.

        Raises different exceptions based on why the video is unavailable,
        otherwise does nothing.
        """
        status, messages = extract.playability_status(self.watch_html)

        for reason in messages:
            if status == 'UNPLAYABLE':
                if reason == (
                    'Join this channel to get access to members-only content '
                    'like this video, and other exclusive perks.'
                ):
                    raise exceptions.MembersOnly(video_id=self.video_id)
                elif reason == 'This live stream recording is not available.':
                    raise exceptions.RecordingUnavailable(video_id=self.video_id)
                else:
                    raise exceptions.VideoUnavailable(video_id=self.video_id)
            elif status == 'LOGIN_REQUIRED':
                if reason == (
                    'This is a private video. '
                    'Please sign in to verify that you may see it.'
                ):
                    raise exceptions.VideoPrivate(video_id=self.video_id)
            elif status == 'ERROR':
                if reason == 'Video unavailable':
                    raise exceptions.VideoUnavailable(video_id=self.video_id)
            elif status == 'LIVE_STREAM':
                raise exceptions.LiveStreamError(video_id=self.video_id)

    @property
    def vid_info(self):
        """Parse the raw vid info and return the parsed result.

        :rtype: Dict[Any, Any]
        """
        if self._vid_info:
            return self._vid_info

        innertube = InnerTube(use_oauth=self.use_oauth, allow_cache=self.allow_oauth_cache)

        innertube_response = innertube.player(self.video_id)
        self._vid_info = innertube_response
        return self._vid_info

    def bypass_age_gate(self):
        """Attempt to update the vid_info by bypassing the age gate."""
        innertube = InnerTube(
            client='ANDROID_EMBED',
            use_oauth=self.use_oauth,
            allow_cache=self.allow_oauth_cache
        )
        innertube_response = innertube.player(self.video_id)

        playability_status = innertube_response['playabilityStatus'].get('status', None)

        # If we still can't access the video, raise an exception
        # (tier 3 age restriction)
        if playability_status == 'UNPLAYABLE':
            raise exceptions.AgeRestrictedError(self.video_id)

        self._vid_info = innertube_response

    @property
    def caption_tracks(self) -> List[pytube.Caption]:
        """Get a list of :class:`Caption <Caption>`.

        :rtype: List[Caption]
        """
        raw_tracks = (
            self.vid_info.get("captions", {})
            .get("playerCaptionsTracklistRenderer", {})
            .get("captionTracks", [])
        )
        return [pytube.Caption(track) for track in raw_tracks]

    @property
    def captions(self) -> pytube.CaptionQuery:
        """Interface to query caption tracks.

        :rtype: :class:`CaptionQuery <CaptionQuery>`.
        """
        return pytube.CaptionQuery(self.caption_tracks)

    @property
    def streams(self) -> StreamQuery:
        """Interface to query both adaptive (DASH) and progressive streams.

        :rtype: :class:`StreamQuery <StreamQuery>`.
        """
        self.check_availability()
        return StreamQuery(self.fmt_streams)

    @property
    def thumbnail_url(self) -> str:
        """Get the thumbnail url image.

        :rtype: str
        """
        thumbnail_details = (
            self.vid_info.get("videoDetails", {})
            .get("thumbnail", {})
            .get("thumbnails")
        )
        if thumbnail_details:
            thumbnail_details = thumbnail_details[-1]  # last item has max size
            return thumbnail_details["url"]

        return f"https://img.youtube.com/vi/{self.video_id}/maxresdefault.jpg"

    @property
    def publish_date(self):
        """Get the publish date.

        :rtype: datetime
        """
        if self._publish_date:
            return self._publish_date
        self._publish_date = extract.publish_date(self.watch_html)
        return self._publish_date

    @publish_date.setter
    def publish_date(self, value):
        """Sets the publish date."""
        self._publish_date = value

    @property
    def title(self) -> str:
        """Get the video title.

        :rtype: str
        """
        if self._title:
            return self._title

        try:
            self._title = self.vid_info['videoDetails']['title']
        except KeyError:
            # Check_availability will raise the correct exception in most cases
            #  if it doesn't, ask for a report.
            self.check_availability()
            raise exceptions.PytubeError(
                (
                    f'Exception while accessing title of {self.watch_url}. '
                    'Please file a bug report at https://github.com/pytube/pytube'
                )
            )

        return self._title

    @title.setter
    def title(self, value):
        """Sets the title value."""
        self._title = value

    @property
    def description(self) -> str:
        """Get the video description.

        :rtype: str
        """
        return self.vid_info.get("videoDetails", {}).get("shortDescription")

    @property
    def rating(self) -> float:
        """Get the video average rating.

        :rtype: float

        """
        return self.vid_info.get("videoDetails", {}).get("averageRating")

    @property
    def length(self) -> int:
        """Get the video length in seconds.

        :rtype: int
        """
        return int(self.vid_info.get('videoDetails', {}).get('lengthSeconds'))

    @property
    def views(self) -> int:
        """Get the number of the times the video has been viewed.

        :rtype: int
        """
        return int(self.vid_info.get("videoDetails", {}).get("viewCount"))

    @property
    def author(self) -> str:
        """Get the video author.
        :rtype: str
        """
        if self._author:
            return self._author
        self._author = self.vid_info.get("videoDetails", {}).get(
            "author", "unknown"
        )
        return self._author

    @author.setter
    def author(self, value):
        """Set the video author."""
        self._author = value

    @property
    def keywords(self) -> List[str]:
        """Get the video keywords.

        :rtype: List[str]
        """
        return self.vid_info.get('videoDetails', {}).get('keywords', [])

    @property
    def channel_id(self) -> str:
        """Get the video poster's channel id.

        :rtype: str
        """
        return self.vid_info.get('videoDetails', {}).get('channelId', None)

    @property
    def channel_url(self) -> str:
        """Construct the channel url for the video's poster from the channel id.

        :rtype: str
        """
        return f'https://www.youtube.com/channel/{self.channel_id}'

    @property
    def metadata(self) -> Optional[YouTubeMetadata]:
        """Get the metadata for the video.

        :rtype: YouTubeMetadata
        """
        if self._metadata:
            return self._metadata
        else:
            self._metadata = extract.metadata(self.initial_data)
            return self._metadata

    def register_on_progress_callback(self, func: Callable[[Any, bytes, int], None]):
        """Register a download progress callback function post initialization.

        :param callable func:
            A callback function that takes ``stream``, ``chunk``,
             and ``bytes_remaining`` as parameters.

        :rtype: None

        """
        self.stream_monostate.on_progress = func

    def register_on_complete_callback(self, func: Callable[[Any, Optional[str]], None]):
        """Register a download complete callback function post initialization.

        :param callable func:
            A callback function that takes ``stream`` and  ``file_path``.

        :rtype: None

        """
        self.stream_monostate.on_complete = func

    @staticmethod
    def from_id(video_id: str) -> "YouTube":
        """Construct a :class:`YouTube <YouTube>` object from a video id.

        :param str video_id:
            The video id of the YouTube video.

        :rtype: :class:`YouTube <YouTube>`
        
        """
        return YouTube(f"https://www.youtube.com/watch?v={video_id}")

```

# pytube/parser.py
```python
import ast
import json
import re
from pytube.exceptions import HTMLParseError


def parse_for_all_objects(html, preceding_regex):
    """Parses input html to find all matches for the input starting point.

    :param str html:
        HTML to be parsed for an object.
    :param str preceding_regex:
        Regex to find the string preceding the object.
    :rtype list:
    :returns:
        A list of dicts created from parsing the objects.
    """
    result = []
    regex = re.compile(preceding_regex)
    match_iter = regex.finditer(html)
    for match in match_iter:
        if match:
            start_index = match.end()
            try:
                obj = parse_for_object_from_startpoint(html, start_index)
            except HTMLParseError:
                # Some of the instances might fail because set is technically
                # a method of the ytcfg object. We'll skip these since they
                # don't seem relevant at the moment.
                continue
            else:
                result.append(obj)

    if len(result) == 0:
        raise HTMLParseError(f'No matches for regex {preceding_regex}')

    return result


def parse_for_object(html, preceding_regex):
    """Parses input html to find the end of a JavaScript object.

    :param str html:
        HTML to be parsed for an object.
    :param str preceding_regex:
        Regex to find the string preceding the object.
    :rtype dict:
    :returns:
        A dict created from parsing the object.
    """
    regex = re.compile(preceding_regex)
    result = regex.search(html)
    if not result:
        raise HTMLParseError(f'No matches for regex {preceding_regex}')

    start_index = result.end()
    return parse_for_object_from_startpoint(html, start_index)


def find_object_from_startpoint(html, start_point):
    """Parses input html to find the end of a JavaScript object.

    :param str html:
        HTML to be parsed for an object.
    :param int start_point:
        Index of where the object starts.
    :rtype dict:
    :returns:
        A dict created from parsing the object.
    """
    html = html[start_point:]
    if html[0] not in ['{','[']:
        raise HTMLParseError(f'Invalid start point. Start of HTML:\n{html[:20]}')

    # First letter MUST be a open brace, so we put that in the stack,
    # and skip the first character.
    last_char = '{'
    curr_char = None
    stack = [html[0]]
    i = 1

    context_closers = {
        '{': '}',
        '[': ']',
        '"': '"',
        '/': '/' # javascript regex
    }

    while i < len(html):
        if len(stack) == 0:
            break
        if curr_char not in [' ', '\n']:
            last_char = curr_char
        curr_char = html[i]
        curr_context = stack[-1]

        # If we've reached a context closer, we can remove an element off the stack
        if curr_char == context_closers[curr_context]:
            stack.pop()
            i += 1
            continue

        # Strings and regex expressions require special context handling because they can contain
        #  context openers *and* closers
        if curr_context in ['"', '/']:
            # If there's a backslash in a string or regex expression, we skip a character
            if curr_char == '\\':
                i += 2
                continue
        else:
            # Non-string contexts are when we need to look for context openers.
            if curr_char in context_closers.keys():
                # Slash starts a regular expression depending on context
                if not (curr_char == '/' and last_char not in ['(', ',', '=', ':', '[', '!', '&', '|', '?', '{', '}', ';']): 
                    stack.append(curr_char)

        i += 1

    full_obj = html[:i]
    return full_obj  # noqa: R504


def parse_for_object_from_startpoint(html, start_point):
    """JSONifies an object parsed from HTML.

    :param str html:
        HTML to be parsed for an object.
    :param int start_point:
        Index of where the object starts.
    :rtype dict:
    :returns:
        A dict created from parsing the object.
    """
    full_obj = find_object_from_startpoint(html, start_point)
    try:
        return json.loads(full_obj)
    except json.decoder.JSONDecodeError:
        try:
            return ast.literal_eval(full_obj)
        except (ValueError, SyntaxError):
            raise HTMLParseError('Could not parse object.')


def throttling_array_split(js_array):
    """Parses the throttling array into a python list of strings.

    Expects input to begin with `[` and close with `]`.

    :param str js_array:
        The javascript array, as a string.
    :rtype: list:
    :returns:
        A list of strings representing splits on `,` in the throttling array.
    """
    results = []
    curr_substring = js_array[1:]

    comma_regex = re.compile(r",")
    func_regex = re.compile(r"function\([^)]*\)")

    while len(curr_substring) > 0:
        if curr_substring.startswith('function'):
            # Handle functions separately. These can contain commas
            match = func_regex.search(curr_substring)
            match_start, match_end = match.span()

            function_text = find_object_from_startpoint(curr_substring, match.span()[1])
            full_function_def = curr_substring[:match_end + len(function_text)]
            results.append(full_function_def)
            curr_substring = curr_substring[len(full_function_def) + 1:]
        else:
            match = comma_regex.search(curr_substring)

            # Try-catch to capture end of array
            try:
                match_start, match_end = match.span()
            except AttributeError:
                match_start = len(curr_substring) - 1
                match_end = match_start + 1

            curr_el = curr_substring[:match_start]
            results.append(curr_el)
            curr_substring = curr_substring[match_end:]

    return results

```

# pytube/metadata.py
```python
"""This module contains the YouTubeMetadata class."""
import json
from typing import Dict, List, Optional


class YouTubeMetadata:
    def __init__(self, metadata: List):
        self._raw_metadata: List = metadata
        self._metadata = [{}]

        for el in metadata:
            # We only add metadata to the dict if it has a simpleText title.
            if 'title' in el and 'simpleText' in el['title']:
                metadata_title = el['title']['simpleText']
            else:
                continue

            contents = el['contents'][0]
            if 'simpleText' in contents:
                self._metadata[-1][metadata_title] = contents['simpleText']
            elif 'runs' in contents:
                self._metadata[-1][metadata_title] = contents['runs'][0]['text']

            # Upon reaching a dividing line, create a new grouping
            if el.get('hasDividerLine', False):
                self._metadata.append({})

        # If we happen to create an empty dict at the end, drop it
        if self._metadata[-1] == {}:
            self._metadata = self._metadata[:-1]

    def __getitem__(self, key):
        return self._metadata[key]

    def __iter__(self):
        for el in self._metadata:
            yield el

    def __str__(self):
        return json.dumps(self._metadata)

    @property
    def raw_metadata(self) -> Optional[Dict]:
        return self._raw_metadata

    @property
    def metadata(self):
        return self._metadata

```

# pytube/streams.py
```python
"""
This module contains a container for stream manifest data.

A container object for the media stream (video only / audio only / video+audio
combined). This was referred to as ``Video`` in the legacy pytube version, but
has been renamed to accommodate DASH (which serves the audio and video
separately).
"""
import logging
import os
from math import ceil

from datetime import datetime
from typing import BinaryIO, Dict, Optional, Tuple
from urllib.error import HTTPError
from urllib.parse import parse_qs

from pytube import extract, request
from pytube.helpers import safe_filename, target_directory
from pytube.itags import get_format_profile
from pytube.monostate import Monostate

logger = logging.getLogger(__name__)


class Stream:
    """Container for stream manifest data."""

    def __init__(
        self, stream: Dict, monostate: Monostate
    ):
        """Construct a :class:`Stream <Stream>`.

        :param dict stream:
            The unscrambled data extracted from YouTube.
        :param dict monostate:
            Dictionary of data shared across all instances of
            :class:`Stream <Stream>`.
        """
        # A dictionary shared between all instances of :class:`Stream <Stream>`
        # (Borg pattern).
        self._monostate = monostate

        self.url = stream["url"]  # signed download url
        self.itag = int(
            stream["itag"]
        )  # stream format id (youtube nomenclature)

        # set type and codec info

        # 'video/webm; codecs="vp8, vorbis"' -> 'video/webm', ['vp8', 'vorbis']
        self.mime_type, self.codecs = extract.mime_type_codec(stream["mimeType"])

        # 'video/webm' -> 'video', 'webm'
        self.type, self.subtype = self.mime_type.split("/")

        # ['vp8', 'vorbis'] -> video_codec: vp8, audio_codec: vorbis. DASH
        # streams return NoneType for audio/video depending.
        self.video_codec, self.audio_codec = self.parse_codecs()

        self.is_otf: bool = stream["is_otf"]
        self.bitrate: Optional[int] = stream["bitrate"]

        # filesize in bytes
        self._filesize: Optional[int] = int(stream.get('contentLength', 0))
        
        # filesize in kilobytes
        self._filesize_kb: Optional[float] = float(ceil(float(stream.get('contentLength', 0)) / 1024 * 1000) / 1000)
        
        # filesize in megabytes
        self._filesize_mb: Optional[float] = float(ceil(float(stream.get('contentLength', 0)) / 1024 / 1024 * 1000) / 1000)
        
        # filesize in gigabytes(fingers crossed we don't need terabytes going forward though)
        self._filesize_gb: Optional[float] = float(ceil(float(stream.get('contentLength', 0)) / 1024 / 1024 / 1024 * 1000) / 1000)

        # Additional information about the stream format, such as resolution,
        # frame rate, and whether the stream is live (HLS) or 3D.
        itag_profile = get_format_profile(self.itag)
        self.is_dash = itag_profile["is_dash"]
        self.abr = itag_profile["abr"]  # average bitrate (audio streams only)
        if 'fps' in stream:
            self.fps = stream['fps']  # Video streams only
        self.resolution = itag_profile[
            "resolution"
        ]  # resolution (e.g.: "480p")
        self.is_3d = itag_profile["is_3d"]
        self.is_hdr = itag_profile["is_hdr"]
        self.is_live = itag_profile["is_live"]

    @property
    def is_adaptive(self) -> bool:
        """Whether the stream is DASH.

        :rtype: bool
        """
        # if codecs has two elements (e.g.: ['vp8', 'vorbis']): 2 % 2 = 0
        # if codecs has one element (e.g.: ['vp8']) 1 % 2 = 1
        return bool(len(self.codecs) % 2)

    @property
    def is_progressive(self) -> bool:
        """Whether the stream is progressive.

        :rtype: bool
        """
        return not self.is_adaptive

    @property
    def includes_audio_track(self) -> bool:
        """Whether the stream only contains audio.

        :rtype: bool
        """
        return self.is_progressive or self.type == "audio"

    @property
    def includes_video_track(self) -> bool:
        """Whether the stream only contains video.

        :rtype: bool
        """
        return self.is_progressive or self.type == "video"

    def parse_codecs(self) -> Tuple[Optional[str], Optional[str]]:
        """Get the video/audio codecs from list of codecs.

        Parse a variable length sized list of codecs and returns a
        constant two element tuple, with the video codec as the first element
        and audio as the second. Returns None if one is not available
        (adaptive only).

        :rtype: tuple
        :returns:
            A two element tuple with audio and video codecs.

        """
        video = None
        audio = None
        if not self.is_adaptive:
            video, audio = self.codecs
        elif self.includes_video_track:
            video = self.codecs[0]
        elif self.includes_audio_track:
            audio = self.codecs[0]
        return video, audio

    @property
    def filesize(self) -> int:
        """File size of the media stream in bytes.

        :rtype: int
        :returns:
            Filesize (in bytes) of the stream.
        """
        if self._filesize == 0:
            try:
                self._filesize = request.filesize(self.url)
            except HTTPError as e:
                if e.code != 404:
                    raise
                self._filesize = request.seq_filesize(self.url)
        return self._filesize
    
    @property
    def filesize_kb(self) -> float:
        """File size of the media stream in kilobytes.

        :rtype: float
        :returns:
            Rounded filesize (in kilobytes) of the stream.
        """
        if self._filesize_kb == 0:
            try:
                self._filesize_kb = float(ceil(request.filesize(self.url)/1024 * 1000) / 1000)
            except HTTPError as e:
                if e.code != 404:
                    raise
                self._filesize_kb = float(ceil(request.seq_filesize(self.url)/1024 * 1000) / 1000)
        return self._filesize_kb
    
    @property
    def filesize_mb(self) -> float:
        """File size of the media stream in megabytes.

        :rtype: float
        :returns:
            Rounded filesize (in megabytes) of the stream.
        """
        if self._filesize_mb == 0:
            try:
                self._filesize_mb = float(ceil(request.filesize(self.url)/1024/1024 * 1000) / 1000)
            except HTTPError as e:
                if e.code != 404:
                    raise
                self._filesize_mb = float(ceil(request.seq_filesize(self.url)/1024/1024 * 1000) / 1000)
        return self._filesize_mb

    @property
    def filesize_gb(self) -> float:
        """File size of the media stream in gigabytes.

        :rtype: float
        :returns:
            Rounded filesize (in gigabytes) of the stream.
        """
        if self._filesize_gb == 0:
            try:
                self._filesize_gb = float(ceil(request.filesize(self.url)/1024/1024/1024 * 1000) / 1000)
            except HTTPError as e:
                if e.code != 404:
                    raise
                self._filesize_gb = float(ceil(request.seq_filesize(self.url)/1024/1024/1024 * 1000) / 1000)
        return self._filesize_gb
    
    @property
    def title(self) -> str:
        """Get title of video

        :rtype: str
        :returns:
            Youtube video title
        """
        return self._monostate.title or "Unknown YouTube Video Title"

    @property
    def filesize_approx(self) -> int:
        """Get approximate filesize of the video

        Falls back to HTTP call if there is not sufficient information to approximate

        :rtype: int
        :returns: size of video in bytes
        """
        if self._monostate.duration and self.bitrate:
            bits_in_byte = 8
            return int(
                (self._monostate.duration * self.bitrate) / bits_in_byte
            )

        return self.filesize

    @property
    def expiration(self) -> datetime:
        expire = parse_qs(self.url.split("?")[1])["expire"][0]
        return datetime.utcfromtimestamp(int(expire))

    @property
    def default_filename(self) -> str:
        """Generate filename based on the video title.

        :rtype: str
        :returns:
            An os file system compatible filename.
        """
        filename = safe_filename(self.title)
        return f"{filename}.{self.subtype}"

    def download(
        self,
        output_path: Optional[str] = None,
        filename: Optional[str] = None,
        filename_prefix: Optional[str] = None,
        skip_existing: bool = True,
        timeout: Optional[int] = None,
        max_retries: Optional[int] = 0
    ) -> str:
        """Write the media stream to disk.

        :param output_path:
            (optional) Output path for writing media file. If one is not
            specified, defaults to the current working directory.
        :type output_path: str or None
        :param filename:
            (optional) Output filename (stem only) for writing media file.
            If one is not specified, the default filename is used.
        :type filename: str or None
        :param filename_prefix:
            (optional) A string that will be prepended to the filename.
            For example a number in a playlist or the name of a series.
            If one is not specified, nothing will be prepended
            This is separate from filename so you can use the default
            filename but still add a prefix.
        :type filename_prefix: str or None
        :param skip_existing:
            (optional) Skip existing files, defaults to True
        :type skip_existing: bool
        :param timeout:
            (optional) Request timeout length in seconds. Uses system default.
        :type timeout: int
        :param max_retries:
            (optional) Number of retries to attempt after socket timeout. Defaults to 0.
        :type max_retries: int
        :returns:
            Path to the saved video
        :rtype: str

        """
        file_path = self.get_file_path(
            filename=filename,
            output_path=output_path,
            filename_prefix=filename_prefix,
        )

        if skip_existing and self.exists_at_path(file_path):
            logger.debug(f'file {file_path} already exists, skipping')
            self.on_complete(file_path)
            return file_path

        bytes_remaining = self.filesize
        logger.debug(f'downloading ({self.filesize} total bytes) file to {file_path}')

        with open(file_path, "wb") as fh:
            try:
                for chunk in request.stream(
                    self.url,
                    timeout=timeout,
                    max_retries=max_retries
                ):
                    # reduce the (bytes) remainder by the length of the chunk.
                    bytes_remaining -= len(chunk)
                    # send to the on_progress callback.
                    self.on_progress(chunk, fh, bytes_remaining)
            except HTTPError as e:
                if e.code != 404:
                    raise
                # Some adaptive streams need to be requested with sequence numbers
                for chunk in request.seq_stream(
                    self.url,
                    timeout=timeout,
                    max_retries=max_retries
                ):
                    # reduce the (bytes) remainder by the length of the chunk.
                    bytes_remaining -= len(chunk)
                    # send to the on_progress callback.
                    self.on_progress(chunk, fh, bytes_remaining)
        self.on_complete(file_path)
        return file_path

    def get_file_path(
        self,
        filename: Optional[str] = None,
        output_path: Optional[str] = None,
        filename_prefix: Optional[str] = None,
    ) -> str:
        if not filename:
            filename = self.default_filename
        if filename_prefix:
            filename = f"{filename_prefix}{filename}"
        return os.path.join(target_directory(output_path), filename)

    def exists_at_path(self, file_path: str) -> bool:
        return (
            os.path.isfile(file_path)
            and os.path.getsize(file_path) == self.filesize
        )

    def stream_to_buffer(self, buffer: BinaryIO) -> None:
        """Write the media stream to buffer

        :rtype: io.BytesIO buffer
        """
        bytes_remaining = self.filesize
        logger.info(
            "downloading (%s total bytes) file to buffer", self.filesize,
        )

        for chunk in request.stream(self.url):
            # reduce the (bytes) remainder by the length of the chunk.
            bytes_remaining -= len(chunk)
            # send to the on_progress callback.
            self.on_progress(chunk, buffer, bytes_remaining)
        self.on_complete(None)

    def on_progress(
        self, chunk: bytes, file_handler: BinaryIO, bytes_remaining: int
    ):
        """On progress callback function.

        This function writes the binary data to the file, then checks if an
        additional callback is defined in the monostate. This is exposed to
        allow things like displaying a progress bar.

        :param bytes chunk:
            Segment of media file binary data, not yet written to disk.
        :param file_handler:
            The file handle where the media is being written to.
        :type file_handler:
            :py:class:`io.BufferedWriter`
        :param int bytes_remaining:
            The delta between the total file size in bytes and amount already
            downloaded.

        :rtype: None

        """
        file_handler.write(chunk)
        logger.debug("download remaining: %s", bytes_remaining)
        if self._monostate.on_progress:
            self._monostate.on_progress(self, chunk, bytes_remaining)

    def on_complete(self, file_path: Optional[str]):
        """On download complete handler function.

        :param file_path:
            The file handle where the media is being written to.
        :type file_path: str

        :rtype: None

        """
        logger.debug("download finished")
        on_complete = self._monostate.on_complete
        if on_complete:
            logger.debug("calling on_complete callback %s", on_complete)
            on_complete(self, file_path)

    def __repr__(self) -> str:
        """Printable object representation.

        :rtype: str
        :returns:
            A string representation of a :class:`Stream <Stream>` object.
        """
        parts = ['itag="{s.itag}"', 'mime_type="{s.mime_type}"']
        if self.includes_video_track:
            parts.extend(['res="{s.resolution}"', 'fps="{s.fps}fps"'])
            if not self.is_adaptive:
                parts.extend(
                    ['vcodec="{s.video_codec}"', 'acodec="{s.audio_codec}"',]
                )
            else:
                parts.extend(['vcodec="{s.video_codec}"'])
        else:
            parts.extend(['abr="{s.abr}"', 'acodec="{s.audio_codec}"'])
        parts.extend(['progressive="{s.is_progressive}"', 'type="{s.type}"'])
        return f"<Stream: {' '.join(parts).format(s=self)}>"

```

# pytube/extract.py
```python
"""This module contains all non-cipher related data extraction logic."""
import logging
import urllib.parse
import re
from collections import OrderedDict
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qs, quote, urlencode, urlparse

from pytube.cipher import Cipher
from pytube.exceptions import HTMLParseError, LiveStreamError, RegexMatchError
from pytube.helpers import regex_search
from pytube.metadata import YouTubeMetadata
from pytube.parser import parse_for_object, parse_for_all_objects


logger = logging.getLogger(__name__)


def publish_date(watch_html: str):
    """Extract publish date
    :param str watch_html:
        The html contents of the watch page.
    :rtype: str
    :returns:
        Publish date of the video.
    """
    try:
        result = regex_search(
            r"(?<=itemprop=\"datePublished\" content=\")\d{4}-\d{2}-\d{2}",
            watch_html, group=0
        )
    except RegexMatchError:
        return None
    return datetime.strptime(result, '%Y-%m-%d')


def recording_available(watch_html):
    """Check if live stream recording is available.

    :param str watch_html:
        The html contents of the watch page.
    :rtype: bool
    :returns:
        Whether or not the content is private.
    """
    unavailable_strings = [
        'This live stream recording is not available.'
    ]
    for string in unavailable_strings:
        if string in watch_html:
            return False
    return True


def is_private(watch_html):
    """Check if content is private.

    :param str watch_html:
        The html contents of the watch page.
    :rtype: bool
    :returns:
        Whether or not the content is private.
    """
    private_strings = [
        "This is a private video. Please sign in to verify that you may see it.",
        "\"simpleText\":\"Private video\"",
        "This video is private."
    ]
    for string in private_strings:
        if string in watch_html:
            return True
    return False


def is_age_restricted(watch_html: str) -> bool:
    """Check if content is age restricted.

    :param str watch_html:
        The html contents of the watch page.
    :rtype: bool
    :returns:
        Whether or not the content is age restricted.
    """
    try:
        regex_search(r"og:restrictions:age", watch_html, group=0)
    except RegexMatchError:
        return False
    return True


def playability_status(watch_html: str) -> (str, str):
    """Return the playability status and status explanation of a video.

    For example, a video may have a status of LOGIN_REQUIRED, and an explanation
    of "This is a private video. Please sign in to verify that you may see it."

    This explanation is what gets incorporated into the media player overlay.

    :param str watch_html:
        The html contents of the watch page.
    :rtype: bool
    :returns:
        Playability status and reason of the video.
    """
    player_response = initial_player_response(watch_html)
    status_dict = player_response.get('playabilityStatus', {})
    if 'liveStreamability' in status_dict:
        return 'LIVE_STREAM', 'Video is a live stream.'
    if 'status' in status_dict:
        if 'reason' in status_dict:
            return status_dict['status'], [status_dict['reason']]
        if 'messages' in status_dict:
            return status_dict['status'], status_dict['messages']
    return None, [None]


def video_id(url: str) -> str:
    """Extract the ``video_id`` from a YouTube url.

    This function supports the following patterns:

    - :samp:`https://youtube.com/watch?v={video_id}`
    - :samp:`https://youtube.com/embed/{video_id}`
    - :samp:`https://youtu.be/{video_id}`

    :param str url:
        A YouTube url containing a video id.
    :rtype: str
    :returns:
        YouTube video id.
    """
    return regex_search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url, group=1)


def playlist_id(url: str) -> str:
    """Extract the ``playlist_id`` from a YouTube url.

    This function supports the following patterns:

    - :samp:`https://youtube.com/playlist?list={playlist_id}`
    - :samp:`https://youtube.com/watch?v={video_id}&list={playlist_id}`

    :param str url:
        A YouTube url containing a playlist id.
    :rtype: str
    :returns:
        YouTube playlist id.
    """
    parsed = urllib.parse.urlparse(url)
    return parse_qs(parsed.query)['list'][0]


def channel_name(url: str) -> str:
    """Extract the ``channel_name`` or ``channel_id`` from a YouTube url.

    This function supports the following patterns:

    - :samp:`https://youtube.com/c/{channel_name}/*`
    - :samp:`https://youtube.com/channel/{channel_id}/*
    - :samp:`https://youtube.com/u/{channel_name}/*`
    - :samp:`https://youtube.com/user/{channel_id}/*

    :param str url:
        A YouTube url containing a channel name.
    :rtype: str
    :returns:
        YouTube channel name.
    """
    patterns = [
        r"(?:\/(c)\/([%\d\w_\-]+)(\/.*)?)",
        r"(?:\/(channel)\/([%\w\d_\-]+)(\/.*)?)",
        r"(?:\/(u)\/([%\d\w_\-]+)(\/.*)?)",
        r"(?:\/(user)\/([%\w\d_\-]+)(\/.*)?)"
    ]
    for pattern in patterns:
        regex = re.compile(pattern)
        function_match = regex.search(url)
        if function_match:
            logger.debug("finished regex search, matched: %s", pattern)
            uri_style = function_match.group(1)
            uri_identifier = function_match.group(2)
            return f'/{uri_style}/{uri_identifier}'

    raise RegexMatchError(
        caller="channel_name", pattern="patterns"
    )


def video_info_url(video_id: str, watch_url: str) -> str:
    """Construct the video_info url.

    :param str video_id:
        A YouTube video identifier.
    :param str watch_url:
        A YouTube watch url.
    :rtype: str
    :returns:
        :samp:`https://youtube.com/get_video_info` with necessary GET
        parameters.
    """
    params = OrderedDict(
        [
            ("video_id", video_id),
            ("ps", "default"),
            ("eurl", quote(watch_url)),
            ("hl", "en_US"),
            ("html5", "1"),
            ("c", "TVHTML5"),
            ("cver", "7.20201028"),
        ]
    )
    return _video_info_url(params)


def video_info_url_age_restricted(video_id: str, embed_html: str) -> str:
    """Construct the video_info url.

    :param str video_id:
        A YouTube video identifier.
    :param str embed_html:
        The html contents of the embed page (for age restricted videos).
    :rtype: str
    :returns:
        :samp:`https://youtube.com/get_video_info` with necessary GET
        parameters.
    """
    try:
        sts = regex_search(r'"sts"\s*:\s*(\d+)', embed_html, group=1)
    except RegexMatchError:
        sts = ""
    # Here we use ``OrderedDict`` so that the output is consistent between
    # Python 2.7+.
    eurl = f"https://youtube.googleapis.com/v/{video_id}"
    params = OrderedDict(
        [
            ("video_id", video_id),
            ("eurl", eurl),
            ("sts", sts),
            ("html5", "1"),
            ("c", "TVHTML5"),
            ("cver", "7.20201028"),
        ]
    )
    return _video_info_url(params)


def _video_info_url(params: OrderedDict) -> str:
    return "https://www.youtube.com/get_video_info?" + urlencode(params)


def js_url(html: str) -> str:
    """Get the base JavaScript url.

    Construct the base JavaScript url, which contains the decipher
    "transforms".

    :param str html:
        The html contents of the watch page.
    """
    try:
        base_js = get_ytplayer_config(html)['assets']['js']
    except (KeyError, RegexMatchError):
        base_js = get_ytplayer_js(html)
    return "https://youtube.com" + base_js


def mime_type_codec(mime_type_codec: str) -> Tuple[str, List[str]]:
    """Parse the type data.

    Breaks up the data in the ``type`` key of the manifest, which contains the
    mime type and codecs serialized together, and splits them into separate
    elements.

    **Example**:

    mime_type_codec('audio/webm; codecs="opus"') -> ('audio/webm', ['opus'])

    :param str mime_type_codec:
        String containing mime type and codecs.
    :rtype: tuple
    :returns:
        The mime type and a list of codecs.

    """
    pattern = r"(\w+\/\w+)\;\scodecs=\"([a-zA-Z-0-9.,\s]*)\""
    regex = re.compile(pattern)
    results = regex.search(mime_type_codec)
    if not results:
        raise RegexMatchError(caller="mime_type_codec", pattern=pattern)
    mime_type, codecs = results.groups()
    return mime_type, [c.strip() for c in codecs.split(",")]


def get_ytplayer_js(html: str) -> Any:
    """Get the YouTube player base JavaScript path.

    :param str html
        The html contents of the watch page.
    :rtype: str
    :returns:
        Path to YouTube's base.js file.
    """
    js_url_patterns = [
        r"(/s/player/[\w\d]+/[\w\d_/.]+/base\.js)"
    ]
    for pattern in js_url_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(html)
        if function_match:
            logger.debug("finished regex search, matched: %s", pattern)
            yt_player_js = function_match.group(1)
            return yt_player_js

    raise RegexMatchError(
        caller="get_ytplayer_js", pattern="js_url_patterns"
    )


def get_ytplayer_config(html: str) -> Any:
    """Get the YouTube player configuration data from the watch html.

    Extract the ``ytplayer_config``, which is json data embedded within the
    watch html and serves as the primary source of obtaining the stream
    manifest data.

    :param str html:
        The html contents of the watch page.
    :rtype: str
    :returns:
        Substring of the html containing the encoded manifest data.
    """
    logger.debug("finding initial function name")
    config_patterns = [
        r"ytplayer\.config\s*=\s*",
        r"ytInitialPlayerResponse\s*=\s*"
    ]
    for pattern in config_patterns:
        # Try each pattern consecutively if they don't find a match
        try:
            return parse_for_object(html, pattern)
        except HTMLParseError as e:
            logger.debug(f'Pattern failed: {pattern}')
            logger.debug(e)
            continue

    # setConfig() needs to be handled a little differently.
    # We want to parse the entire argument to setConfig()
    #  and use then load that as json to find PLAYER_CONFIG
    #  inside of it.
    setconfig_patterns = [
        r"yt\.setConfig\(.*['\"]PLAYER_CONFIG['\"]:\s*"
    ]
    for pattern in setconfig_patterns:
        # Try each pattern consecutively if they don't find a match
        try:
            return parse_for_object(html, pattern)
        except HTMLParseError:
            continue

    raise RegexMatchError(
        caller="get_ytplayer_config", pattern="config_patterns, setconfig_patterns"
    )


def get_ytcfg(html: str) -> str:
    """Get the entirety of the ytcfg object.

    This is built over multiple pieces, so we have to find all matches and
    combine the dicts together.

    :param str html:
        The html contents of the watch page.
    :rtype: str
    :returns:
        Substring of the html containing the encoded manifest data.
    """
    ytcfg = {}
    ytcfg_patterns = [
        r"ytcfg\s=\s",
        r"ytcfg\.set\("
    ]
    for pattern in ytcfg_patterns:
        # Try each pattern consecutively and try to build a cohesive object
        try:
            found_objects = parse_for_all_objects(html, pattern)
            for obj in found_objects:
                ytcfg.update(obj)
        except HTMLParseError:
            continue

    if len(ytcfg) > 0:
        return ytcfg

    raise RegexMatchError(
        caller="get_ytcfg", pattern="ytcfg_pattenrs"
    )


def apply_signature(stream_manifest: Dict, vid_info: Dict, js: str) -> None:
    """Apply the decrypted signature to the stream manifest.

    :param dict stream_manifest:
        Details of the media streams available.
    :param str js:
        The contents of the base.js asset file.

    """
    cipher = Cipher(js=js)

    for i, stream in enumerate(stream_manifest):
        try:
            url: str = stream["url"]
        except KeyError:
            live_stream = (
                vid_info.get("playabilityStatus", {},)
                .get("liveStreamability")
            )
            if live_stream:
                raise LiveStreamError("UNKNOWN")
        # 403 Forbidden fix.
        if "signature" in url or (
            "s" not in stream and ("&sig=" in url or "&lsig=" in url)
        ):
            # For certain videos, YouTube will just provide them pre-signed, in
            # which case there's no real magic to download them and we can skip
            # the whole signature descrambling entirely.
            logger.debug("signature found, skip decipher")
            continue

        signature = cipher.get_signature(ciphered_signature=stream["s"])

        logger.debug(
            "finished descrambling signature for itag=%s", stream["itag"]
        )
        parsed_url = urlparse(url)

        # Convert query params off url to dict
        query_params = parse_qs(urlparse(url).query)
        query_params = {
            k: v[0] for k,v in query_params.items()
        }
        query_params['sig'] = signature
        if 'ratebypass' not in query_params.keys():
            # Cipher n to get the updated value

            initial_n = list(query_params['n'])
            new_n = cipher.calculate_n(initial_n)
            query_params['n'] = new_n

        url = f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?{urlencode(query_params)}'  # noqa:E501

        # 403 forbidden fix
        stream_manifest[i]["url"] = url


def apply_descrambler(stream_data: Dict) -> None:
    """Apply various in-place transforms to YouTube's media stream data.

    Creates a ``list`` of dictionaries by string splitting on commas, then
    taking each list item, parsing it as a query string, converting it to a
    ``dict`` and unquoting the value.

    :param dict stream_data:
        Dictionary containing query string encoded values.

    **Example**:

    >>> d = {'foo': 'bar=1&var=test,em=5&t=url%20encoded'}
    >>> apply_descrambler(d, 'foo')
    >>> print(d)
    {'foo': [{'bar': '1', 'var': 'test'}, {'em': '5', 't': 'url encoded'}]}

    """
    if 'url' in stream_data:
        return None

    # Merge formats and adaptiveFormats into a single list
    formats = []
    if 'formats' in stream_data.keys():
        formats.extend(stream_data['formats'])
    if 'adaptiveFormats' in stream_data.keys():
        formats.extend(stream_data['adaptiveFormats'])

    # Extract url and s from signatureCiphers as necessary
    for data in formats:
        if 'url' not in data:
            if 'signatureCipher' in data:
                cipher_url = parse_qs(data['signatureCipher'])
                data['url'] = cipher_url['url'][0]
                data['s'] = cipher_url['s'][0]
        data['is_otf'] = data.get('type') == 'FORMAT_STREAM_TYPE_OTF'

    logger.debug("applying descrambler")
    return formats


def initial_data(watch_html: str) -> str:
    """Extract the ytInitialData json from the watch_html page.

    This mostly contains metadata necessary for rendering the page on-load,
    such as video information, copyright notices, etc.

    @param watch_html: Html of the watch page
    @return:
    """
    patterns = [
        r"window\[['\"]ytInitialData['\"]]\s*=\s*",
        r"ytInitialData\s*=\s*"
    ]
    for pattern in patterns:
        try:
            return parse_for_object(watch_html, pattern)
        except HTMLParseError:
            pass

    raise RegexMatchError(caller='initial_data', pattern='initial_data_pattern')


def initial_player_response(watch_html: str) -> str:
    """Extract the ytInitialPlayerResponse json from the watch_html page.

    This mostly contains metadata necessary for rendering the page on-load,
    such as video information, copyright notices, etc.

    @param watch_html: Html of the watch page
    @return:
    """
    patterns = [
        r"window\[['\"]ytInitialPlayerResponse['\"]]\s*=\s*",
        r"ytInitialPlayerResponse\s*=\s*"
    ]
    for pattern in patterns:
        try:
            return parse_for_object(watch_html, pattern)
        except HTMLParseError:
            pass

    raise RegexMatchError(
        caller='initial_player_response',
        pattern='initial_player_response_pattern'
    )


def metadata(initial_data) -> Optional[YouTubeMetadata]:
    """Get the informational metadata for the video.

    e.g.:
    [
        {
            'Song': '강남스타일(Gangnam Style)',
            'Artist': 'PSY',
            'Album': 'PSY SIX RULES Pt.1',
            'Licensed to YouTube by': 'YG Entertainment Inc. [...]'
        }
    ]

    :rtype: YouTubeMetadata
    """
    try:
        metadata_rows: List = initial_data["contents"]["twoColumnWatchNextResults"][
            "results"]["results"]["contents"][1]["videoSecondaryInfoRenderer"][
            "metadataRowContainer"]["metadataRowContainerRenderer"]["rows"]
    except (KeyError, IndexError):
        # If there's an exception accessing this data, it probably doesn't exist.
        return YouTubeMetadata([])

    # Rows appear to only have "metadataRowRenderer" or "metadataRowHeaderRenderer"
    #  and we only care about the former, so we filter the others
    metadata_rows = filter(
        lambda x: "metadataRowRenderer" in x.keys(),
        metadata_rows
    )

    # We then access the metadataRowRenderer key in each element
    #  and build a metadata object from this new list
    metadata_rows = [x["metadataRowRenderer"] for x in metadata_rows]

    return YouTubeMetadata(metadata_rows)

```

# pytube/helpers.py
```python
"""Various helper functions implemented by pytube."""
import functools
import gzip
import json
import logging
import os
import re
import warnings
from typing import Any, Callable, Dict, List, Optional, TypeVar
from urllib import request

from pytube.exceptions import RegexMatchError

logger = logging.getLogger(__name__)


class DeferredGeneratorList:
    """A wrapper class for deferring list generation.

    Pytube has some continuation generators that create web calls, which means
    that any time a full list is requested, all of those web calls must be
    made at once, which could lead to slowdowns. This will allow individual
    elements to be queried, so that slowdowns only happen as necessary. For
    example, you can iterate over elements in the list without accessing them
    all simultaneously. This should allow for speed improvements for playlist
    and channel interactions.
    """
    def __init__(self, generator):
        """Construct a :class:`DeferredGeneratorList <DeferredGeneratorList>`.

        :param generator generator:
            The deferrable generator to create a wrapper for.
        :param func func:
            (Optional) A function to call on the generator items to produce the list.
        """
        self.gen = generator
        self._elements = []

    def __eq__(self, other):
        """We want to mimic list behavior for comparison."""
        return list(self) == other

    def __getitem__(self, key) -> Any:
        """Only generate items as they're asked for."""
        # We only allow querying with indexes.
        if not isinstance(key, (int, slice)):
            raise TypeError('Key must be either a slice or int.')

        # Convert int keys to slice
        key_slice = key
        if isinstance(key, int):
            key_slice = slice(key, key + 1, 1)

        # Generate all elements up to the final item
        while len(self._elements) < key_slice.stop:
            try:
                next_item = next(self.gen)
            except StopIteration:
                # If we can't find enough elements for the slice, raise an IndexError
                raise IndexError
            else:
                self._elements.append(next_item)

        return self._elements[key]

    def __iter__(self):
        """Custom iterator for dynamically generated list."""
        iter_index = 0
        while True:
            try:
                curr_item = self[iter_index]
            except IndexError:
                return
            else:
                yield curr_item
                iter_index += 1

    def __next__(self) -> Any:
        """Fetch next element in iterator."""
        try:
            curr_element = self[self.iter_index]
        except IndexError:
            raise StopIteration
        self.iter_index += 1
        return curr_element  # noqa:R504

    def __len__(self) -> int:
        """Return length of list of all items."""
        self.generate_all()
        return len(self._elements)

    def __repr__(self) -> str:
        """String representation of all items."""
        self.generate_all()
        return str(self._elements)

    def __reversed__(self):
        self.generate_all()
        return self._elements[::-1]

    def generate_all(self):
        """Generate all items."""
        while True:
            try:
                next_item = next(self.gen)
            except StopIteration:
                break
            else:
                self._elements.append(next_item)


def regex_search(pattern: str, string: str, group: int) -> str:
    """Shortcut method to search a string for a given pattern.

    :param str pattern:
        A regular expression pattern.
    :param str string:
        A target string to search.
    :param int group:
        Index of group to return.
    :rtype:
        str or tuple
    :returns:
        Substring pattern matches.
    """
    regex = re.compile(pattern)
    results = regex.search(string)
    if not results:
        raise RegexMatchError(caller="regex_search", pattern=pattern)

    logger.debug("matched regex search: %s", pattern)

    return results.group(group)


def safe_filename(s: str, max_length: int = 255) -> str:
    """Sanitize a string making it safe to use as a filename.

    This function was based off the limitations outlined here:
    https://en.wikipedia.org/wiki/Filename.

    :param str s:
        A string to make safe for use as a file name.
    :param int max_length:
        The maximum filename character length.
    :rtype: str
    :returns:
        A sanitized string.
    """
    # Characters in range 0-31 (0x00-0x1F) are not allowed in ntfs filenames.
    ntfs_characters = [chr(i) for i in range(0, 31)]
    characters = [
        r'"',
        r"\#",
        r"\$",
        r"\%",
        r"'",
        r"\*",
        r"\,",
        r"\.",
        r"\/",
        r"\:",
        r'"',
        r"\;",
        r"\<",
        r"\>",
        r"\?",
        r"\\",
        r"\^",
        r"\|",
        r"\~",
        r"\\\\",
    ]
    pattern = "|".join(ntfs_characters + characters)
    regex = re.compile(pattern, re.UNICODE)
    filename = regex.sub("", s)
    return filename[:max_length].rsplit(" ", 0)[0]


def setup_logger(level: int = logging.ERROR, log_filename: Optional[str] = None) -> None:
    """Create a configured instance of logger.

    :param int level:
        Describe the severity level of the logs to handle.
    """
    fmt = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    date_fmt = "%H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    # https://github.com/pytube/pytube/issues/163
    logger = logging.getLogger("pytube")
    logger.setLevel(level)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if log_filename is not None:
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


GenericType = TypeVar("GenericType")


def cache(func: Callable[..., GenericType]) -> GenericType:
    """ mypy compatible annotation wrapper for lru_cache"""
    return functools.lru_cache()(func)  # type: ignore


def deprecated(reason: str) -> Callable:
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    """

    def decorator(func1):
        message = "Call to deprecated function {name} ({reason})."

        @functools.wraps(func1)
        def new_func1(*args, **kwargs):
            warnings.simplefilter("always", DeprecationWarning)
            warnings.warn(
                message.format(name=func1.__name__, reason=reason),
                category=DeprecationWarning,
                stacklevel=2,
            )
            warnings.simplefilter("default", DeprecationWarning)
            return func1(*args, **kwargs)

        return new_func1

    return decorator


def target_directory(output_path: Optional[str] = None) -> str:
    """
    Function for determining target directory of a download.
    Returns an absolute path (if relative one given) or the current
    path (if none given). Makes directory if it does not exist.

    :type output_path: str
        :rtype: str
    :returns:
        An absolute directory path as a string.
    """
    if output_path:
        if not os.path.isabs(output_path):
            output_path = os.path.join(os.getcwd(), output_path)
    else:
        output_path = os.getcwd()
    os.makedirs(output_path, exist_ok=True)
    return output_path


def install_proxy(proxy_handler: Dict[str, str]) -> None:
    proxy_support = request.ProxyHandler(proxy_handler)
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)


def uniqueify(duped_list: List) -> List:
    """Remove duplicate items from a list, while maintaining list order.

    :param List duped_list
        List to remove duplicates from

    :return List result
        De-duplicated list
    """
    seen: Dict[Any, bool] = {}
    result = []
    for item in duped_list:
        if item in seen:
            continue
        seen[item] = True
        result.append(item)
    return result


def generate_all_html_json_mocks():
    """Regenerate the video mock json files for all current test videos.

    This should automatically output to the test/mocks directory.
    """
    test_vid_ids = [
        '2lAe1cqCOXo',
        '5YceQ8YqYMc',
        'irauhITDrsE',
        'm8uHb5jIGN8',
        'QRS8MkLhQmM',
        'WXxV9g7lsFE'
    ]
    for vid_id in test_vid_ids:
        create_mock_html_json(vid_id)


def create_mock_html_json(vid_id) -> Dict[str, Any]:
    """Generate a json.gz file with sample html responses.

    :param str vid_id
        YouTube video id

    :return dict data
        Dict used to generate the json.gz file
    """
    from pytube import YouTube
    gzip_filename = 'yt-video-%s-html.json.gz' % vid_id

    # Get the pytube directory in order to navigate to /tests/mocks
    pytube_dir_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir
        )
    )
    pytube_mocks_path = os.path.join(pytube_dir_path, 'tests', 'mocks')
    gzip_filepath = os.path.join(pytube_mocks_path, gzip_filename)

    yt = YouTube(f'https://www.youtube.com/watch?v={vid_id}')
    html_data = {
        'url': yt.watch_url,
        'js': yt.js,
        'embed_html': yt.embed_html,
        'watch_html': yt.watch_html,
        'vid_info': yt.vid_info
    }

    logger.info(f'Outputing json.gz file to {gzip_filepath}')
    with gzip.open(gzip_filepath, 'wb') as f:
        f.write(json.dumps(html_data).encode('utf-8'))

    return html_data

```

# pytube/query.py
```python
"""This module provides a query interface for media streams and captions."""
from collections.abc import Mapping, Sequence
from typing import Callable, List, Optional, Union

from pytube import Caption, Stream
from pytube.helpers import deprecated


class StreamQuery(Sequence):
    """Interface for querying the available media streams."""

    def __init__(self, fmt_streams):
        """Construct a :class:`StreamQuery <StreamQuery>`.

        param list fmt_streams:
            list of :class:`Stream <Stream>` instances.
        """
        self.fmt_streams = fmt_streams
        self.itag_index = {int(s.itag): s for s in fmt_streams}

    def filter(
        self,
        fps=None,
        res=None,
        resolution=None,
        mime_type=None,
        type=None,
        subtype=None,
        file_extension=None,
        abr=None,
        bitrate=None,
        video_codec=None,
        audio_codec=None,
        only_audio=None,
        only_video=None,
        progressive=None,
        adaptive=None,
        is_dash=None,
        custom_filter_functions=None,
    ):
        """Apply the given filtering criterion.

        :param fps:
            (optional) The frames per second.
        :type fps:
            int or None

        :param resolution:
            (optional) Alias to ``res``.
        :type res:
            str or None

        :param res:
            (optional) The video resolution.
        :type resolution:
            str or None

        :param mime_type:
            (optional) Two-part identifier for file formats and format contents
            composed of a "type", a "subtype".
        :type mime_type:
            str or None

        :param type:
            (optional) Type part of the ``mime_type`` (e.g.: audio, video).
        :type type:
            str or None

        :param subtype:
            (optional) Sub-type part of the ``mime_type`` (e.g.: mp4, mov).
        :type subtype:
            str or None

        :param file_extension:
            (optional) Alias to ``sub_type``.
        :type file_extension:
            str or None

        :param abr:
            (optional) Average bitrate (ABR) refers to the average amount of
            data transferred per unit of time (e.g.: 64kbps, 192kbps).
        :type abr:
            str or None

        :param bitrate:
            (optional) Alias to ``abr``.
        :type bitrate:
            str or None

        :param video_codec:
            (optional) Video compression format.
        :type video_codec:
            str or None

        :param audio_codec:
            (optional) Audio compression format.
        :type audio_codec:
            str or None

        :param bool progressive:
            Excludes adaptive streams (one file contains both audio and video
            tracks).

        :param bool adaptive:
            Excludes progressive streams (audio and video are on separate
            tracks).

        :param bool is_dash:
            Include/exclude dash streams.

        :param bool only_audio:
            Excludes streams with video tracks.

        :param bool only_video:
            Excludes streams with audio tracks.

        :param custom_filter_functions:
            (optional) Interface for defining complex filters without
            subclassing.
        :type custom_filter_functions:
            list or None

        """
        filters = []
        if res or resolution:
            if isinstance(res, str) or isinstance(resolution, str):
                filters.append(lambda s: s.resolution == (res or resolution))
            elif isinstance(res, list) or isinstance(resolution, list):
                filters.append(lambda s: s.resolution in (res or resolution))

        if fps:
            filters.append(lambda s: s.fps == fps)

        if mime_type:
            filters.append(lambda s: s.mime_type == mime_type)

        if type:
            filters.append(lambda s: s.type == type)

        if subtype or file_extension:
            filters.append(lambda s: s.subtype == (subtype or file_extension))

        if abr or bitrate:
            filters.append(lambda s: s.abr == (abr or bitrate))

        if video_codec:
            filters.append(lambda s: s.video_codec == video_codec)

        if audio_codec:
            filters.append(lambda s: s.audio_codec == audio_codec)

        if only_audio:
            filters.append(
                lambda s: (
                    s.includes_audio_track and not s.includes_video_track
                ),
            )

        if only_video:
            filters.append(
                lambda s: (
                    s.includes_video_track and not s.includes_audio_track
                ),
            )

        if progressive:
            filters.append(lambda s: s.is_progressive)

        if adaptive:
            filters.append(lambda s: s.is_adaptive)

        if custom_filter_functions:
            filters.extend(custom_filter_functions)

        if is_dash is not None:
            filters.append(lambda s: s.is_dash == is_dash)

        return self._filter(filters)

    def _filter(self, filters: List[Callable]) -> "StreamQuery":
        fmt_streams = self.fmt_streams
        for filter_lambda in filters:
            fmt_streams = filter(filter_lambda, fmt_streams)
        return StreamQuery(list(fmt_streams))

    def order_by(self, attribute_name: str) -> "StreamQuery":
        """Apply a sort order. Filters out stream the do not have the attribute.

        :param str attribute_name:
            The name of the attribute to sort by.
        """
        has_attribute = [
            s
            for s in self.fmt_streams
            if getattr(s, attribute_name) is not None
        ]
        # Check that the attributes have string values.
        if has_attribute and isinstance(
            getattr(has_attribute[0], attribute_name), str
        ):
            # Try to return a StreamQuery sorted by the integer representations
            # of the values.
            try:
                return StreamQuery(
                    sorted(
                        has_attribute,
                        key=lambda s: int(
                            "".join(
                                filter(str.isdigit, getattr(s, attribute_name))
                            )
                        ),  # type: ignore  # noqa: E501
                    )
                )
            except ValueError:
                pass

        return StreamQuery(
            sorted(has_attribute, key=lambda s: getattr(s, attribute_name))
        )

    def desc(self) -> "StreamQuery":
        """Sort streams in descending order.

        :rtype: :class:`StreamQuery <StreamQuery>`

        """
        return StreamQuery(self.fmt_streams[::-1])

    def asc(self) -> "StreamQuery":
        """Sort streams in ascending order.

        :rtype: :class:`StreamQuery <StreamQuery>`

        """
        return self

    def get_by_itag(self, itag: int) -> Optional[Stream]:
        """Get the corresponding :class:`Stream <Stream>` for a given itag.

        :param int itag:
            YouTube format identifier code.
        :rtype: :class:`Stream <Stream>` or None
        :returns:
            The :class:`Stream <Stream>` matching the given itag or None if
            not found.

        """
        return self.itag_index.get(int(itag))

    def get_by_resolution(self, resolution: str) -> Optional[Stream]:
        """Get the corresponding :class:`Stream <Stream>` for a given resolution.

        Stream must be a progressive mp4.

        :param str resolution:
            Video resolution i.e. "720p", "480p", "360p", "240p", "144p"
        :rtype: :class:`Stream <Stream>` or None
        :returns:
            The :class:`Stream <Stream>` matching the given itag or None if
            not found.

        """
        return self.filter(
            progressive=True, subtype="mp4", resolution=resolution
        ).first()

    def get_lowest_resolution(self) -> Optional[Stream]:
        """Get lowest resolution stream that is a progressive mp4.

        :rtype: :class:`Stream <Stream>` or None
        :returns:
            The :class:`Stream <Stream>` matching the given itag or None if
            not found.

        """
        return (
            self.filter(progressive=True, subtype="mp4")
            .order_by("resolution")
            .first()
        )

    def get_highest_resolution(self) -> Optional[Stream]:
        """Get highest resolution stream that is a progressive video.

        :rtype: :class:`Stream <Stream>` or None
        :returns:
            The :class:`Stream <Stream>` matching the given itag or None if
            not found.

        """
        return self.filter(progressive=True).order_by("resolution").last()

    def get_audio_only(self, subtype: str = "mp4") -> Optional[Stream]:
        """Get highest bitrate audio stream for given codec (defaults to mp4)

        :param str subtype:
            Audio subtype, defaults to mp4
        :rtype: :class:`Stream <Stream>` or None
        :returns:
            The :class:`Stream <Stream>` matching the given itag or None if
            not found.
        """
        return (
            self.filter(only_audio=True, subtype=subtype)
            .order_by("abr")
            .last()
        )

    def otf(self, is_otf: bool = False) -> "StreamQuery":
        """Filter stream by OTF, useful if some streams have 404 URLs

        :param bool is_otf: Set to False to retrieve only non-OTF streams
        :rtype: :class:`StreamQuery <StreamQuery>`
        :returns: A StreamQuery object with otf filtered streams
        """
        return self._filter([lambda s: s.is_otf == is_otf])

    def first(self) -> Optional[Stream]:
        """Get the first :class:`Stream <Stream>` in the results.

        :rtype: :class:`Stream <Stream>` or None
        :returns:
            the first result of this query or None if the result doesn't
            contain any streams.

        """
        try:
            return self.fmt_streams[0]
        except IndexError:
            return None

    def last(self):
        """Get the last :class:`Stream <Stream>` in the results.

        :rtype: :class:`Stream <Stream>` or None
        :returns:
            Return the last result of this query or None if the result
            doesn't contain any streams.

        """
        try:
            return self.fmt_streams[-1]
        except IndexError:
            pass

    @deprecated("Get the size of this list directly using len()")
    def count(self, value: Optional[str] = None) -> int:  # pragma: no cover
        """Get the count of items in the list.

        :rtype: int
        """
        if value:
            return self.fmt_streams.count(value)

        return len(self)

    @deprecated("This object can be treated as a list, all() is useless")
    def all(self) -> List[Stream]:  # pragma: no cover
        """Get all the results represented by this query as a list.

        :rtype: list

        """
        return self.fmt_streams

    def __getitem__(self, i: Union[slice, int]):
        return self.fmt_streams[i]

    def __len__(self) -> int:
        return len(self.fmt_streams)

    def __repr__(self) -> str:
        return f"{self.fmt_streams}"


class CaptionQuery(Mapping):
    """Interface for querying the available captions."""

    def __init__(self, captions: List[Caption]):
        """Construct a :class:`Caption <Caption>`.

        param list captions:
            list of :class:`Caption <Caption>` instances.

        """
        self.lang_code_index = {c.code: c for c in captions}

    @deprecated(
        "This object can be treated as a dictionary, i.e. captions['en']"
    )
    def get_by_language_code(
        self, lang_code: str
    ) -> Optional[Caption]:  # pragma: no cover
        """Get the :class:`Caption <Caption>` for a given ``lang_code``.

        :param str lang_code:
            The code that identifies the caption language.
        :rtype: :class:`Caption <Caption>` or None
        :returns:
            The :class:`Caption <Caption>` matching the given ``lang_code`` or
            None if it does not exist.
        """
        return self.lang_code_index.get(lang_code)

    @deprecated("This object can be treated as a dictionary")
    def all(self) -> List[Caption]:  # pragma: no cover
        """Get all the results represented by this query as a list.

        :rtype: list

        """
        return list(self.lang_code_index.values())

    def __getitem__(self, i: str):
        return self.lang_code_index[i]

    def __len__(self) -> int:
        return len(self.lang_code_index)

    def __iter__(self):
        return iter(self.lang_code_index.values())

    def __repr__(self) -> str:
        return f"{self.lang_code_index}"

```

# pytube/cipher.py
```python
"""
This module contains all logic necessary to decipher the signature.

YouTube's strategy to restrict downloading videos is to send a ciphered version
of the signature to the client, along with the decryption algorithm obfuscated
in JavaScript. For the clients to play the videos, JavaScript must take the
ciphered version, cycle it through a series of "transform functions," and then
signs the media URL with the output.

This module is responsible for (1) finding and extracting those "transform
functions" (2) maps them to Python equivalents and (3) taking the ciphered
signature and decoding it.

"""
import logging
import re
from itertools import chain
from typing import Any, Callable, Dict, List, Optional, Tuple

from pytube.exceptions import ExtractError, RegexMatchError
from pytube.helpers import cache, regex_search
from pytube.parser import find_object_from_startpoint, throttling_array_split

logger = logging.getLogger(__name__)


class Cipher:
    def __init__(self, js: str):
        self.transform_plan: List[str] = get_transform_plan(js)
        var_regex = re.compile(r"^\w+\W")
        var_match = var_regex.search(self.transform_plan[0])
        if not var_match:
            raise RegexMatchError(
                caller="__init__", pattern=var_regex.pattern
            )
        var = var_match.group(0)[:-1]
        self.transform_map = get_transform_map(js, var)
        self.js_func_patterns = [
            r"\w+\.(\w+)\(\w,(\d+)\)",
            r"\w+\[(\"\w+\")\]\(\w,(\d+)\)"
        ]

        self.throttling_plan = get_throttling_plan(js)
        self.throttling_array = get_throttling_function_array(js)

        self.calculated_n = None

    def calculate_n(self, initial_n: list):
        """Converts n to the correct value to prevent throttling."""
        if self.calculated_n:
            return self.calculated_n

        # First, update all instances of 'b' with the list(initial_n)
        for i in range(len(self.throttling_array)):
            if self.throttling_array[i] == 'b':
                self.throttling_array[i] = initial_n

        for step in self.throttling_plan:
            curr_func = self.throttling_array[int(step[0])]
            if not callable(curr_func):
                logger.debug(f'{curr_func} is not callable.')
                logger.debug(f'Throttling array:\n{self.throttling_array}\n')
                raise ExtractError(f'{curr_func} is not callable.')

            first_arg = self.throttling_array[int(step[1])]

            if len(step) == 2:
                curr_func(first_arg)
            elif len(step) == 3:
                second_arg = self.throttling_array[int(step[2])]
                curr_func(first_arg, second_arg)

        self.calculated_n = ''.join(initial_n)
        return self.calculated_n

    def get_signature(self, ciphered_signature: str) -> str:
        """Decipher the signature.

        Taking the ciphered signature, applies the transform functions.

        :param str ciphered_signature:
            The ciphered signature sent in the ``player_config``.
        :rtype: str
        :returns:
            Decrypted signature required to download the media content.
        """
        signature = list(ciphered_signature)

        for js_func in self.transform_plan:
            name, argument = self.parse_function(js_func)  # type: ignore
            signature = self.transform_map[name](signature, argument)
            logger.debug(
                "applied transform function\n"
                "output: %s\n"
                "js_function: %s\n"
                "argument: %d\n"
                "function: %s",
                "".join(signature),
                name,
                argument,
                self.transform_map[name],
            )

        return "".join(signature)

    @cache
    def parse_function(self, js_func: str) -> Tuple[str, int]:
        """Parse the Javascript transform function.

        Break a JavaScript transform function down into a two element ``tuple``
        containing the function name and some integer-based argument.

        :param str js_func:
            The JavaScript version of the transform function.
        :rtype: tuple
        :returns:
            two element tuple containing the function name and an argument.

        **Example**:

        parse_function('DE.AJ(a,15)')
        ('AJ', 15)

        """
        logger.debug("parsing transform function")
        for pattern in self.js_func_patterns:
            regex = re.compile(pattern)
            parse_match = regex.search(js_func)
            if parse_match:
                fn_name, fn_arg = parse_match.groups()
                return fn_name, int(fn_arg)

        raise RegexMatchError(
            caller="parse_function", pattern="js_func_patterns"
        )


def get_initial_function_name(js: str) -> str:
    """Extract the name of the function responsible for computing the signature.
    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        Function name from regex match
    """

    function_patterns = [
        r"\b[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*encodeURIComponent\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\b[a-zA-Z0-9]+\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*encodeURIComponent\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r'(?:\b|[^a-zA-Z0-9$])(?P<sig>[a-zA-Z0-9$]{2})\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)',  # noqa: E501
        r'(?P<sig>[a-zA-Z0-9$]+)\s*=\s*function\(\s*a\s*\)\s*{\s*a\s*=\s*a\.split\(\s*""\s*\)',  # noqa: E501
        r'(["\'])signature\1\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(',
        r"\.sig\|\|(?P<sig>[a-zA-Z0-9$]+)\(",
        r"yt\.akamaized\.net/\)\s*\|\|\s*.*?\s*[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*(?:encodeURIComponent\s*\()?\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\b[cs]\s*&&\s*[adf]\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\b[a-zA-Z0-9]+\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\bc\s*&&\s*a\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\bc\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
        r"\bc\s*&&\s*[a-zA-Z0-9]+\.set\([^,]+\s*,\s*\([^)]*\)\s*\(\s*(?P<sig>[a-zA-Z0-9$]+)\(",  # noqa: E501
    ]
    logger.debug("finding initial function name")
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            logger.debug("finished regex search, matched: %s", pattern)
            return function_match.group(1)

    raise RegexMatchError(
        caller="get_initial_function_name", pattern="multiple"
    )


def get_transform_plan(js: str) -> List[str]:
    """Extract the "transform plan".

    The "transform plan" is the functions that the ciphered signature is
    cycled through to obtain the actual signature.

    :param str js:
        The contents of the base.js asset file.

    **Example**:

    ['DE.AJ(a,15)',
    'DE.VR(a,3)',
    'DE.AJ(a,51)',
    'DE.VR(a,3)',
    'DE.kT(a,51)',
    'DE.kT(a,8)',
    'DE.VR(a,3)',
    'DE.kT(a,21)']
    """
    name = re.escape(get_initial_function_name(js))
    pattern = r"%s=function\(\w\){[a-z=\.\(\"\)]*;(.*);(?:.+)}" % name
    logger.debug("getting transform plan")
    return regex_search(pattern, js, group=1).split(";")


def get_transform_object(js: str, var: str) -> List[str]:
    """Extract the "transform object".

    The "transform object" contains the function definitions referenced in the
    "transform plan". The ``var`` argument is the obfuscated variable name
    which contains these functions, for example, given the function call
    ``DE.AJ(a,15)`` returned by the transform plan, "DE" would be the var.

    :param str js:
        The contents of the base.js asset file.
    :param str var:
        The obfuscated variable name that stores an object with all functions
        that descrambles the signature.

    **Example**:

    >>> get_transform_object(js, 'DE')
    ['AJ:function(a){a.reverse()}',
    'VR:function(a,b){a.splice(0,b)}',
    'kT:function(a,b){var c=a[0];a[0]=a[b%a.length];a[b]=c}']

    """
    pattern = r"var %s={(.*?)};" % re.escape(var)
    logger.debug("getting transform object")
    regex = re.compile(pattern, flags=re.DOTALL)
    transform_match = regex.search(js)
    if not transform_match:
        raise RegexMatchError(caller="get_transform_object", pattern=pattern)

    return transform_match.group(1).replace("\n", " ").split(", ")


def get_transform_map(js: str, var: str) -> Dict:
    """Build a transform function lookup.

    Build a lookup table of obfuscated JavaScript function names to the
    Python equivalents.

    :param str js:
        The contents of the base.js asset file.
    :param str var:
        The obfuscated variable name that stores an object with all functions
        that descrambles the signature.

    """
    transform_object = get_transform_object(js, var)
    mapper = {}
    for obj in transform_object:
        # AJ:function(a){a.reverse()} => AJ, function(a){a.reverse()}
        name, function = obj.split(":", 1)
        fn = map_functions(function)
        mapper[name] = fn
    return mapper


def get_throttling_function_name(js: str) -> str:
    """Extract the name of the function that computes the throttling parameter.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    function_patterns = [
        # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
        # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
        # var Bpa = [iha];
        # ...
        # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
        # Bpa.length || iha("")) }};
        # In the above case, `iha` is the relevant function name
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&\s*'
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    ]
    logger.debug('Finding throttling function name')
    for pattern in function_patterns:
        regex = re.compile(pattern)
        function_match = regex.search(js)
        if function_match:
            logger.debug("finished regex search, matched: %s", pattern)
            if len(function_match.groups()) == 1:
                return function_match.group(1)
            idx = function_match.group(2)
            if idx:
                idx = idx.strip("[]")
                array = re.search(
                    r'var {nfunc}\s*=\s*(\[.+?\]);'.format(
                        nfunc=re.escape(function_match.group(1))),
                    js
                )
                if array:
                    array = array.group(1).strip("[]").split(",")
                    array = [x.strip() for x in array]
                    return array[int(idx)]

    raise RegexMatchError(
        caller="get_throttling_function_name", pattern="multiple"
    )


def get_throttling_function_code(js: str) -> str:
    """Extract the raw code for the throttling function.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    # Begin by extracting the correct function name
    name = re.escape(get_throttling_function_name(js))

    # Identify where the function is defined
    pattern_start = r"%s=function\(\w\)" % name
    regex = re.compile(pattern_start)
    match = regex.search(js)

    # Extract the code within curly braces for the function itself, and merge any split lines
    code_lines_list = find_object_from_startpoint(js, match.span()[1]).split('\n')
    joined_lines = "".join(code_lines_list)

    # Prepend function definition (e.g. `Dea=function(a)`)
    return match.group(0) + joined_lines


def get_throttling_function_array(js: str) -> List[Any]:
    """Extract the "c" array.

    :param str js:
        The contents of the base.js asset file.
    :returns:
        The array of various integers, arrays, and functions.
    """
    raw_code = get_throttling_function_code(js)

    array_start = r",c=\["
    array_regex = re.compile(array_start)
    match = array_regex.search(raw_code)

    array_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)
    str_array = throttling_array_split(array_raw)

    converted_array = []
    for el in str_array:
        try:
            converted_array.append(int(el))
            continue
        except ValueError:
            # Not an integer value.
            pass

        if el == 'null':
            converted_array.append(None)
            continue

        if el.startswith('"') and el.endswith('"'):
            # Convert e.g. '"abcdef"' to string without quotation marks, 'abcdef'
            converted_array.append(el[1:-1])
            continue

        if el.startswith('function'):
            mapper = (
                (r"{for\(\w=\(\w%\w\.length\+\w\.length\)%\w\.length;\w--;\)\w\.unshift\(\w.pop\(\)\)}", throttling_unshift),  # noqa:E501
                (r"{\w\.reverse\(\)}", throttling_reverse),
                (r"{\w\.push\(\w\)}", throttling_push),
                (r";var\s\w=\w\[0\];\w\[0\]=\w\[\w\];\w\[\w\]=\w}", throttling_swap),
                (r"case\s\d+", throttling_cipher_function),
                (r"\w\.splice\(0,1,\w\.splice\(\w,1,\w\[0\]\)\[0\]\)", throttling_nested_splice),  # noqa:E501
                (r";\w\.splice\(\w,1\)}", js_splice),
                (r"\w\.splice\(-\w\)\.reverse\(\)\.forEach\(function\(\w\){\w\.unshift\(\w\)}\)", throttling_prepend),  # noqa:E501
                (r"for\(var \w=\w\.length;\w;\)\w\.push\(\w\.splice\(--\w,1\)\[0\]\)}", throttling_reverse),  # noqa:E501
            )

            found = False
            for pattern, fn in mapper:
                if re.search(pattern, el):
                    converted_array.append(fn)
                    found = True
            if found:
                continue

        converted_array.append(el)

    # Replace null elements with array itself
    for i in range(len(converted_array)):
        if converted_array[i] is None:
            converted_array[i] = converted_array

    return converted_array


def get_throttling_plan(js: str):
    """Extract the "throttling plan".

    The "throttling plan" is a list of tuples used for calling functions
    in the c array. The first element of the tuple is the index of the
    function to call, and any remaining elements of the tuple are arguments
    to pass to that function.

    :param str js:
        The contents of the base.js asset file.
    :returns:
        The full function code for computing the throttlign parameter.
    """
    raw_code = get_throttling_function_code(js)

    transform_start = r"try{"
    plan_regex = re.compile(transform_start)
    match = plan_regex.search(raw_code)

    transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)

    # Steps are either c[x](c[y]) or c[x](c[y],c[z])
    step_start = r"c\[(\d+)\]\(c\[(\d+)\](,c(\[(\d+)\]))?\)"
    step_regex = re.compile(step_start)
    matches = step_regex.findall(transform_plan_raw)
    transform_steps = []
    for match in matches:
        if match[4] != '':
            transform_steps.append((match[0],match[1],match[4]))
        else:
            transform_steps.append((match[0],match[1]))

    return transform_steps


def reverse(arr: List, _: Optional[Any]):
    """Reverse elements in a list.

    This function is equivalent to:

    .. code-block:: javascript

        function(a, b) { a.reverse() }

    This method takes an unused ``b`` variable as their transform functions
    universally sent two arguments.

    **Example**:

    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    return arr[::-1]


def splice(arr: List, b: int):
    """Add/remove items to/from a list.

    This function is equivalent to:

    .. code-block:: javascript

        function(a, b) { a.splice(0, b) }

    **Example**:

    >>> splice([1, 2, 3, 4], 2)
    [1, 2]
    """
    return arr[b:]


def swap(arr: List, b: int):
    """Swap positions at b modulus the list length.

    This function is equivalent to:

    .. code-block:: javascript

        function(a, b) { var c=a[0];a[0]=a[b%a.length];a[b]=c }

    **Example**:

    >>> swap([1, 2, 3, 4], 2)
    [3, 2, 1, 4]
    """
    r = b % len(arr)
    return list(chain([arr[r]], arr[1:r], [arr[0]], arr[r + 1 :]))


def throttling_reverse(arr: list):
    """Reverses the input list.

    Needs to do an in-place reversal so that the passed list gets changed.
    To accomplish this, we create a reversed copy, and then change each
    indvidual element.
    """
    reverse_copy = arr.copy()[::-1]
    for i in range(len(reverse_copy)):
        arr[i] = reverse_copy[i]


def throttling_push(d: list, e: Any):
    """Pushes an element onto a list."""
    d.append(e)


def throttling_mod_func(d: list, e: int):
    """Perform the modular function from the throttling array functions.

    In the javascript, the modular operation is as follows:
    e = (e % d.length + d.length) % d.length

    We simply translate this to python here.
    """
    return (e % len(d) + len(d)) % len(d)


def throttling_unshift(d: list, e: int):
    """Rotates the elements of the list to the right.

    In the javascript, the operation is as follows:
    for(e=(e%d.length+d.length)%d.length;e--;)d.unshift(d.pop())
    """
    e = throttling_mod_func(d, e)
    new_arr = d[-e:] + d[:-e]
    d.clear()
    for el in new_arr:
        d.append(el)


def throttling_cipher_function(d: list, e: str):
    """This ciphers d with e to generate a new list.

    In the javascript, the operation is as follows:
    var h = [A-Za-z0-9-_], f = 96;  // simplified from switch-case loop
    d.forEach(
        function(l,m,n){
            this.push(
                n[m]=h[
                    (h.indexOf(l)-h.indexOf(this[m])+m-32+f--)%h.length
                ]
            )
        },
        e.split("")
    )
    """
    h = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_')
    f = 96
    # by naming it "this" we can more closely reflect the js
    this = list(e)

    # This is so we don't run into weirdness with enumerate while
    #  we change the input list
    copied_list = d.copy()

    for m, l in enumerate(copied_list):
        bracket_val = (h.index(l) - h.index(this[m]) + m - 32 + f) % len(h)
        this.append(
            h[bracket_val]
        )
        d[m] = h[bracket_val]
        f -= 1


def throttling_nested_splice(d: list, e: int):
    """Nested splice function in throttling js.

    In the javascript, the operation is as follows:
    function(d,e){
        e=(e%d.length+d.length)%d.length;
        d.splice(
            0,
            1,
            d.splice(
                e,
                1,
                d[0]
            )[0]
        )
    }

    While testing, all this seemed to do is swap element 0 and e,
    but the actual process is preserved in case there was an edge
    case that was not considered.
    """
    e = throttling_mod_func(d, e)
    inner_splice = js_splice(
        d,
        e,
        1,
        d[0]
    )
    js_splice(
        d,
        0,
        1,
        inner_splice[0]
    )


def throttling_prepend(d: list, e: int):
    """

    In the javascript, the operation is as follows:
    function(d,e){
        e=(e%d.length+d.length)%d.length;
        d.splice(-e).reverse().forEach(
            function(f){
                d.unshift(f)
            }
        )
    }

    Effectively, this moves the last e elements of d to the beginning.
    """
    start_len = len(d)
    # First, calculate e
    e = throttling_mod_func(d, e)

    # Then do the prepending
    new_arr = d[-e:] + d[:-e]

    # And update the input list
    d.clear()
    for el in new_arr:
        d.append(el)

    end_len = len(d)
    assert start_len == end_len


def throttling_swap(d: list, e: int):
    """Swap positions of the 0'th and e'th elements in-place."""
    e = throttling_mod_func(d, e)
    f = d[0]
    d[0] = d[e]
    d[e] = f


def js_splice(arr: list, start: int, delete_count=None, *items):
    """Implementation of javascript's splice function.

    :param list arr:
        Array to splice
    :param int start:
        Index at which to start changing the array
    :param int delete_count:
        Number of elements to delete from the array
    :param *items:
        Items to add to the array

    Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice  # noqa:E501
    """
    # Special conditions for start value
    try:
        if start > len(arr):
            start = len(arr)
        # If start is negative, count backwards from end
        if start < 0:
            start = len(arr) - start
    except TypeError:
        # Non-integer start values are treated as 0 in js
        start = 0

    # Special condition when delete_count is greater than remaining elements
    if not delete_count or delete_count >= len(arr) - start:
        delete_count = len(arr) - start  # noqa: N806

    deleted_elements = arr[start:start + delete_count]

    # Splice appropriately.
    new_arr = arr[:start] + list(items) + arr[start + delete_count:]

    # Replace contents of input array
    arr.clear()
    for el in new_arr:
        arr.append(el)

    return deleted_elements


def map_functions(js_func: str) -> Callable:
    """For a given JavaScript transform function, return the Python equivalent.

    :param str js_func:
        The JavaScript version of the transform function.
    """
    mapper = (
        # function(a){a.reverse()}
        (r"{\w\.reverse\(\)}", reverse),
        # function(a,b){a.splice(0,b)}
        (r"{\w\.splice\(0,\w\)}", splice),
        # function(a,b){var c=a[0];a[0]=a[b%a.length];a[b]=c}
        (r"{var\s\w=\w\[0\];\w\[0\]=\w\[\w\%\w.length\];\w\[\w\]=\w}", swap),
        # function(a,b){var c=a[0];a[0]=a[b%a.length];a[b%a.length]=c}
        (
            r"{var\s\w=\w\[0\];\w\[0\]=\w\[\w\%\w.length\];\w\[\w\%\w.length\]=\w}",
            swap,
        ),
    )

    for pattern, fn in mapper:
        if re.search(pattern, js_func):
            return fn
    raise RegexMatchError(caller="map_functions", pattern="multiple")

```

# pytube/exceptions.py
```python
"""Library specific exception definitions."""
from typing import Pattern, Union


class PytubeError(Exception):
    """Base pytube exception that all others inherit.

    This is done to not pollute the built-in exceptions, which *could* result
    in unintended errors being unexpectedly and incorrectly handled within
    implementers code.
    """


class MaxRetriesExceeded(PytubeError):
    """Maximum number of retries exceeded."""


class HTMLParseError(PytubeError):
    """HTML could not be parsed"""


class ExtractError(PytubeError):
    """Data extraction based exception."""


class RegexMatchError(ExtractError):
    """Regex pattern did not return any matches."""

    def __init__(self, caller: str, pattern: Union[str, Pattern]):
        """
        :param str caller:
            Calling function
        :param str pattern:
            Pattern that failed to match
        """
        super().__init__(f"{caller}: could not find match for {pattern}")
        self.caller = caller
        self.pattern = pattern


class VideoUnavailable(PytubeError):
    """Base video unavailable error."""
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.error_string)

    @property
    def error_string(self):
        return f'{self.video_id} is unavailable'


class AgeRestrictedError(VideoUnavailable):
    """Video is age restricted, and cannot be accessed without OAuth."""
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.video_id)

    @property
    def error_string(self):
        return f"{self.video_id} is age restricted, and can't be accessed without logging in."


class LiveStreamError(VideoUnavailable):
    """Video is a live stream."""
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.video_id)

    @property
    def error_string(self):
        return f'{self.video_id} is streaming live and cannot be loaded'


class VideoPrivate(VideoUnavailable):
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.video_id)

    @property
    def error_string(self):
        return f'{self.video_id} is a private video'


class RecordingUnavailable(VideoUnavailable):
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.video_id)

    @property
    def error_string(self):
        return f'{self.video_id} does not have a live stream recording available'


class MembersOnly(VideoUnavailable):
    """Video is members-only.

    YouTube has special videos that are only viewable to users who have
    subscribed to a content creator.
    ref: https://support.google.com/youtube/answer/7544492?hl=en
    """
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.video_id)

    @property
    def error_string(self):
        return f'{self.video_id} is a members-only video'


class VideoRegionBlocked(VideoUnavailable):
    def __init__(self, video_id: str):
        """
        :param str video_id:
            A YouTube video identifier.
        """
        self.video_id = video_id
        super().__init__(self.video_id)

    @property
    def error_string(self):
        return f'{self.video_id} is not available in your region'

```

# tests/contrib/test_playlist.py
```python
import datetime
from unittest import mock

from pytube import Playlist


@mock.patch("pytube.request.get")
def test_title(request_get, playlist_long_html):
    request_get.return_value = playlist_long_html
    url = (
        "https://www.fakeurl.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ"
        "-ghgoSH6n"
    )
    pl = Playlist(url)
    pl_title = pl.title
    assert (
        pl_title
        == "Python Tutorial for Beginners (For Absolute Beginners)"
    )


@mock.patch("pytube.request.get")
def test_init_with_playlist_url(request_get):
    request_get.return_value = ""
    url = (
        "https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ"
        "-ghgoSH6n"
    )
    playlist = Playlist(url)
    assert playlist.playlist_url == url


@mock.patch("pytube.request.get")
def test_init_with_watch_url(request_get):
    request_get.return_value = ""
    url = (
        "https://www.youtube.com/watch?v=1KeYzjILqDo&"
        "list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n&index=2&t=661s"
    )
    playlist = Playlist(url)
    assert (
        playlist.playlist_url == "https://www.youtube.com/playlist?list"
        "=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n"
    )


@mock.patch("pytube.request.get")
def test_last_updated(request_get, playlist_long_html):
    expected = datetime.date(2020, 10, 8)
    request_get.return_value = playlist_long_html
    playlist = Playlist(
        "https://www.youtube.com/playlist?list"
        "=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n"
    )
    assert playlist.last_updated == expected


@mock.patch("pytube.request.get")
def test_video_urls(request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = playlist_html
    playlist = Playlist(url)
    assert playlist.video_urls == [
        "https://www.youtube.com/watch?v=ujTCoH21GlA",
        "https://www.youtube.com/watch?v=45ryDIPHdGg",
        "https://www.youtube.com/watch?v=1BYu65vLKdA",
        "https://www.youtube.com/watch?v=3AQ_74xrch8",
        "https://www.youtube.com/watch?v=ddqQUz9mZaM",
        "https://www.youtube.com/watch?v=vwLT6bZrHEE",
        "https://www.youtube.com/watch?v=TQKI0KE-JYY",
        "https://www.youtube.com/watch?v=dNBvQ38MlT8",
        "https://www.youtube.com/watch?v=JHxyrMgOUWI",
        "https://www.youtube.com/watch?v=l2I8NycJMCY",
        "https://www.youtube.com/watch?v=g1Zbuk1gAfk",
        "https://www.youtube.com/watch?v=zixd-si9Q-o",
    ]
    request_get.assert_called()


@mock.patch("pytube.request.get")
def test_html(request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = playlist_html
    playlist = Playlist(url)
    assert playlist.html == playlist_html
    request_get.assert_called()


@mock.patch("pytube.request.get")
def test_repr(request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = playlist_html
    playlist = Playlist(url)
    assert (
        repr(playlist) == "["
        "'https://www.youtube.com/watch?v=ujTCoH21GlA', "
        "'https://www.youtube.com/watch?v=45ryDIPHdGg', "
        "'https://www.youtube.com/watch?v=1BYu65vLKdA', "
        "'https://www.youtube.com/watch?v=3AQ_74xrch8', "
        "'https://www.youtube.com/watch?v=ddqQUz9mZaM', "
        "'https://www.youtube.com/watch?v=vwLT6bZrHEE', "
        "'https://www.youtube.com/watch?v=TQKI0KE-JYY', "
        "'https://www.youtube.com/watch?v=dNBvQ38MlT8', "
        "'https://www.youtube.com/watch?v=JHxyrMgOUWI', "
        "'https://www.youtube.com/watch?v=l2I8NycJMCY', "
        "'https://www.youtube.com/watch?v=g1Zbuk1gAfk', "
        "'https://www.youtube.com/watch?v=zixd-si9Q-o'"
        "]"
    )
    request_get.assert_called()


@mock.patch("pytube.request.get")
def test_sequence(request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = playlist_html
    playlist = Playlist(url)
    assert playlist[0] == "https://www.youtube.com/watch?v=ujTCoH21GlA"
    assert len(playlist) == 12


@mock.patch("pytube.request.get")
@mock.patch("pytube.cli.YouTube.__init__", return_value=None)
def test_videos(youtube, request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = playlist_html
    playlist = Playlist(url)
    assert len(list(playlist.videos)) == 12
    request_get.assert_called()


@mock.patch("pytube.request.get")
@mock.patch("pytube.cli.YouTube.__init__", return_value=None)
def test_load_more(youtube, request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.side_effect = [
        playlist_html,
        '{"content_html":"", "load_more_widget_html":""}',
    ]
    playlist = Playlist(url)
    assert len(list(playlist.videos)) == 12
    request_get.assert_called()


@mock.patch("pytube.request.get")
@mock.patch("pytube.contrib.playlist.install_proxy", return_value=None)
def test_proxy(install_proxy, request_get):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = ""
    Playlist(url, proxies={"http": "things"})
    install_proxy.assert_called_with({"http": "things"})


@mock.patch("pytube.request.get")
def test_trimmed(request_get, playlist_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.return_value = playlist_html
    playlist = Playlist(url)
    trimmed = list(playlist.trimmed("1BYu65vLKdA"))
    assert trimmed == [
        "https://www.youtube.com/watch?v=ujTCoH21GlA",
        "https://www.youtube.com/watch?v=45ryDIPHdGg",
    ]
    assert request_get.call_count == 1


@mock.patch("pytube.request.get")
@mock.patch("pytube.request.post")
def test_playlist_failed_pagination(request_post, request_get, playlist_long_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.side_effect = [
        playlist_long_html,
    ]
    request_post.side_effect = [
        "{}"
    ]
    playlist = Playlist(url)
    video_urls = playlist.video_urls
    assert len(video_urls) == 100
    assert request_get.call_count == 1
    assert request_post.call_count == 1
    # TODO: Cannot get this test to work probably
    # request_get.assert_called_with(
    #    "https://www.youtube.com/browse_ajax?ctoken" # noqa
    #    "=4qmFsgIsEhpWTFVVYS12aW9HaGUyYnRCY1puZWFQb25LQRoOZWdaUVZEcERSMUUlM0Q" # noqa
    #    "%3D&continuation" # noqa
    #    "=4qmFsgIsEhpWTFVVYS12aW9HaGUyYnRCY1puZWFQb25LQRoOZWdaUVZEcERSMUUlM0Q" # noqa
    #    "%3D", # noqa
    #    {"extra_headers": {'X-YouTube-Client-Name': '1',
    #                       'X-YouTube-Client-Version': '2.20200720.00.02'}}
    # ) # noqa


@mock.patch("pytube.request.get")
@mock.patch("pytube.request.post")
def test_playlist_pagination(request_post, request_get, playlist_html, playlist_long_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.side_effect = [
        playlist_long_html
    ]
    request_post.side_effect = [
        '{"content_html":"<a '
        'href=\\"/watch?v=BcWz41-4cDk&amp;feature=plpp_video&amp;ved'
        '=CCYQxjQYACITCO33n5-pn-cCFUG3xAodLogN2yj6LA\\">}", '
        '"load_more_widget_html":""}',
        "{}",
    ]
    playlist = Playlist(url)
    assert len(playlist.video_urls) == 100
    assert request_get.call_count == 1
    assert request_post.call_count == 1


@mock.patch("pytube.request.get")
def test_trimmed_pagination(request_get, playlist_html, playlist_long_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.side_effect = [
        playlist_long_html,
        '{"content_html":"<a '
        'href=\\"/watch?v=BcWz41-4cDk&amp;feature=plpp_video&amp;ved'
        '=CCYQxjQYACITCO33n5-pn-cCFUG3xAodLogN2yj6LA\\">}", '
        '"load_more_widget_html":""}',
        "{}",
    ]
    playlist = Playlist(url)
    assert len(list(playlist.trimmed("GTpl5yq3bvk"))) == 3
    assert request_get.call_count == 1


# TODO: Test case not clear to me
@mock.patch("pytube.request.get")
def test_trimmed_pagination_not_found(
    request_get, playlist_html, playlist_long_html
):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.side_effect = [
        playlist_long_html,
        '{"content_html":"<a '
        'href=\\"/watch?v=BcWz41-4cDk&amp;feature=plpp_video&amp;ved'
        '=CCYQxjQYACITCO33n5-pn-cCFUG3xAodLogN2yj6LA\\">}", '
        '"load_more_widget_html":""}',
        "{}",
    ]
    playlist = Playlist(url) # noqa
    # assert len(list(playlist.trimmed("wont-be-found"))) == 101 # noqa
    assert True


# test case for playlist with submenus
@mock.patch("pytube.request.get")
def test_playlist_submenu(request_get, playlist_submenu_html):
    url = "https://www.fakeurl.com/playlist?list=whatever"
    request_get.side_effect = [
        playlist_submenu_html,
        '{"content_html":"<a '
        'href=\\"/watch?v=BcWz41-4cDk&amp;feature=plpp_video&amp;ved'
        '=CCYQxjQYACITCO33n5-pn-cCFUG3xAodLogN2yj6LA\\">}", '
        '"load_more_widget_html":""}',
        "{}",
    ]
    playlist = Playlist(url)
    assert len(playlist.video_urls) == 12


@mock.patch("pytube.request.get")
def test_playlist_length(request_get, playlist_long_html):
    url = 'https://www.example.com/playlist?list=whatever'
    request_get.return_value = playlist_long_html
    p = Playlist(url)
    assert p.length == 217


@mock.patch("pytube.request.get")
def test_playlist_description(request_get, playlist_long_html):
    url = 'https://www.example.com/playlist?list=whatever'
    request_get.return_value = playlist_long_html
    p = Playlist(url)
    assert p.description == (
        'Python Object Oriented - Learning Python in '
        "simple and easy steps ,python,xml,script,install, A beginner's "
        'tutorial containing complete knowledge of Python Syntax Object '
        'Oriented Language, Methods, Tuples,Learn,Python,Tutorial,Interactive,'
        'Free, Tools/Utilities,Getting the most popular pages from your Apache'
        ' logfile,Make your life easier with Virtualenvwrapper,This site now '
        'runs on Django,PythonForBeginners.com has a new owner,How to use '
        'Pillow, a fork of PIL,How to use the Python Imaging Library,Python '
        'Websites and Tutorials,How to use Envoy,Using Feedparser in Python,'
        'Subprocess and Shell Commands in Python, Exceptions Handling, '
        'Sockets, GUI, Extentions, XML Programming'
    )


@mock.patch("pytube.request.get")
def test_playlist_views(request_get, playlist_long_html):
    url = 'https://www.example.com/playlist?list=whatever'
    request_get.return_value = playlist_long_html
    p = Playlist(url)
    assert p.views == 4617130


@mock.patch("pytube.request.get")
def test_playlist_owner(request_get, playlist_long_html):
    url = 'https://www.example.com/playlist?list=whatever'
    request_get.return_value = playlist_long_html
    p = Playlist(url)
    assert p.owner == 'ProgrammingKnowledge'


@mock.patch("pytube.request.get")
def test_playlist_owner_id(request_get, playlist_long_html):
    url = 'https://www.example.com/playlist?list=whatever'
    request_get.return_value = playlist_long_html
    p = Playlist(url)
    assert p.owner_id == 'UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch("pytube.request.get")
def test_playlist_owner_url(request_get, playlist_long_html):
    url = 'https://www.example.com/playlist?list=whatever'
    request_get.return_value = playlist_long_html
    p = Playlist(url)
    assert p.owner_url == 'https://www.youtube.com/channel/UCs6nmQViDpUw0nuIx9c_WvA'

```

# tests/contrib/test_channel.py
```python
from unittest import mock

from pytube import Channel


@mock.patch('pytube.request.get')
def test_init_with_url(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html
    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_url == 'https://www.youtube.com/c/ProgrammingKnowledge'
    assert c.videos_url == f'{c.channel_url}/videos'
    assert c.playlists_url == f'{c.channel_url}/playlists'
    assert c.community_url == f'{c.channel_url}/community'
    assert c.featured_channels_url == f'{c.channel_url}/channels'
    assert c.about_url == f'{c.channel_url}/about'


@mock.patch('pytube.request.get')
def test_channel_uri(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_uri == '/c/ProgrammingKnowledge'

    c = Channel('https://www.youtube.com/channel/UCs6nmQViDpUw0nuIx9c_WvA/videos')
    assert c.channel_uri == '/channel/UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch('pytube.request.get')
def test_channel_name(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_name == 'ProgrammingKnowledge'


@mock.patch('pytube.request.get')
def test_channel_id(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.channel_id == 'UCs6nmQViDpUw0nuIx9c_WvA'


@mock.patch('pytube.request.get')
def test_channel_vanity_url(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    assert c.vanity_url == 'http://www.youtube.com/c/ProgrammingKnowledge'


@mock.patch('pytube.request.get')
def test_channel_video_list(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge/videos')
    first_ten = [
        'https://www.youtube.com/watch?v=t_xLpJo_35k',
        'https://www.youtube.com/watch?v=ccbh5YhxouQ',
        'https://www.youtube.com/watch?v=wDnFjDjxW_0',
        'https://www.youtube.com/watch?v=F3W_p_4XftA',
        'https://www.youtube.com/watch?v=_fxm0xGGEi4',
        'https://www.youtube.com/watch?v=cRbKZzcuIsg',
        'https://www.youtube.com/watch?v=sdDu3dfIuow',
        'https://www.youtube.com/watch?v=10KIbp-gJCE',
        'https://www.youtube.com/watch?v=wZIT-cRtd6s',
        'https://www.youtube.com/watch?v=KucCvEbTj0w',
    ]
    assert c.video_urls[:10] == first_ten


@mock.patch('pytube.request.get')
def test_videos_html(request_get, channel_videos_html):
    request_get.return_value = channel_videos_html

    c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
    assert c.html == channel_videos_html

# Because the Channel object subclasses the Playlist object, most of the tests
# are already taken care of by the Playlist test suite.

```

# .github/ISSUE_TEMPLATE/feature_request.md
```markdown
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: enhancement
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.

```

# .github/ISSUE_TEMPLATE/bug_report.md
```markdown
---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: bug
assignees: ''

---
**Before creating an issue**

Please confirm that you are on the latest version of pytube by installing from the source.
You can do this by running `python -m pip install git+https://github.com/pytube/pytube`.
Sometimes, the pypi library repository is not up to date, and your issue may have been fixed already!

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Please provide the following information:
- The video or playlist url that is causing the error.
- The code where the problem is occurring.

**Expected behavior**
A clear and concise description of what you expected to happen.

**Output**
If pytube raises an exception, please provide the full traceback for the exception.

**System information**
Please provide the following information:
- Python version (run `python --version`)
- Pytube version (run `print(pytube.__version__)` in python)
- Command used to install pytube

```

# .github/workflows/greetings.yml
```yaml
name: Greetings

on: [issues]

jobs:
  greeting:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/first-interaction@v1
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        issue-message: 'Thank you for contributing to PyTube. Please remember to reference [Contributing.md](https://github.com/pytube/pytube/blob/master/Contributing.md)'

```

# .github/workflows/ci.yml
```yaml
name: CI tests

on:
  pull_request:
    branches: [ master ]
    paths-ignore:
      - '**/README.md'
      - 'docs/**'

jobs:
  ci:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python: [3.7, 3.8, 3.9, 3.11]

    steps:
      - name: Checkout repo
        uses: actions/checkout@v2

      - name: Setup python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python }}

      - name: Upgrade pip
        run: pip install --upgrade pip pipenv

      - name: Install pipenv
        run: pipenv install --dev --skip-lock --python ${{ matrix.python }}

      - name: Run make ci
        run: make ci

```

# .github/workflows/pypi-publish.yml
```yaml
# .github/workflows/pypi-publish.yml
name: Publish to PyPI

on:
  release:
    types: [ created ]

jobs:
  deploy:
    if: github.actor == 'nficano' || github.actor == 'RONNCC' || github.actor == 'tfdahlin'
    name: Build Python distribution and publish to PyPI
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2
      - name: Setup python 3.8
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build setuptools wheel twine

      - name: Build and publish
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: |
          python -m build
          python -m twine upload dist/*

```

# pytube/contrib/__init__.py
```python

```

# pytube/contrib/channel.py
```python
# -*- coding: utf-8 -*-
"""Module for interacting with a user's youtube channel."""
import json
import logging
from typing import Dict, List, Optional, Tuple

from pytube import extract, Playlist, request
from pytube.helpers import uniqueify

logger = logging.getLogger(__name__)


class Channel(Playlist):
    def __init__(self, url: str, proxies: Optional[Dict[str, str]] = None):
        """Construct a :class:`Channel <Channel>`.

        :param str url:
            A valid YouTube channel URL.
        :param proxies:
            (Optional) A dictionary of proxies to use for web requests.
        """
        super().__init__(url, proxies)

        self.channel_uri = extract.channel_name(url)

        self.channel_url = (
            f"https://www.youtube.com{self.channel_uri}"
        )

        self.videos_url = self.channel_url + '/videos'
        self.playlists_url = self.channel_url + '/playlists'
        self.community_url = self.channel_url + '/community'
        self.featured_channels_url = self.channel_url + '/channels'
        self.about_url = self.channel_url + '/about'

        # Possible future additions
        self._playlists_html = None
        self._community_html = None
        self._featured_channels_html = None
        self._about_html = None

    @property
    def channel_name(self):
        """Get the name of the YouTube channel.

        :rtype: str
        """
        return self.initial_data['metadata']['channelMetadataRenderer']['title']

    @property
    def channel_id(self):
        """Get the ID of the YouTube channel.

        This will return the underlying ID, not the vanity URL.

        :rtype: str
        """
        return self.initial_data['metadata']['channelMetadataRenderer']['externalId']

    @property
    def vanity_url(self):
        """Get the vanity URL of the YouTube channel.

        Returns None if it doesn't exist.

        :rtype: str
        """
        return self.initial_data['metadata']['channelMetadataRenderer'].get('vanityChannelUrl', None)  # noqa:E501

    @property
    def html(self):
        """Get the html for the /videos page.

        :rtype: str
        """
        if self._html:
            return self._html
        self._html = request.get(self.videos_url)
        return self._html

    @property
    def playlists_html(self):
        """Get the html for the /playlists page.

        Currently unused for any functionality.

        :rtype: str
        """
        if self._playlists_html:
            return self._playlists_html
        else:
            self._playlists_html = request.get(self.playlists_url)
            return self._playlists_html

    @property
    def community_html(self):
        """Get the html for the /community page.

        Currently unused for any functionality.

        :rtype: str
        """
        if self._community_html:
            return self._community_html
        else:
            self._community_html = request.get(self.community_url)
            return self._community_html

    @property
    def featured_channels_html(self):
        """Get the html for the /channels page.

        Currently unused for any functionality.

        :rtype: str
        """
        if self._featured_channels_html:
            return self._featured_channels_html
        else:
            self._featured_channels_html = request.get(self.featured_channels_url)
            return self._featured_channels_html

    @property
    def about_html(self):
        """Get the html for the /about page.

        Currently unused for any functionality.

        :rtype: str
        """
        if self._about_html:
            return self._about_html
        else:
            self._about_html = request.get(self.about_url)
            return self._about_html

    @staticmethod
    def _extract_videos(raw_json: str) -> Tuple[List[str], Optional[str]]:
        """Extracts videos from a raw json page

        :param str raw_json: Input json extracted from the page or the last
            server response
        :rtype: Tuple[List[str], Optional[str]]
        :returns: Tuple containing a list of up to 100 video watch ids and
            a continuation token, if more videos are available
        """
        initial_data = json.loads(raw_json)
        # this is the json tree structure, if the json was extracted from
        # html
        try:
            videos = initial_data["contents"][
                "twoColumnBrowseResultsRenderer"][
                "tabs"][1]["tabRenderer"]["content"][
                "sectionListRenderer"]["contents"][0][
                "itemSectionRenderer"]["contents"][0][
                "gridRenderer"]["items"]
        except (KeyError, IndexError, TypeError):
            try:
                # this is the json tree structure, if the json was directly sent
                # by the server in a continuation response
                important_content = initial_data[1]['response']['onResponseReceivedActions'][
                    0
                ]['appendContinuationItemsAction']['continuationItems']
                videos = important_content
            except (KeyError, IndexError, TypeError):
                try:
                    # this is the json tree structure, if the json was directly sent
                    # by the server in a continuation response
                    # no longer a list and no longer has the "response" key
                    important_content = initial_data['onResponseReceivedActions'][0][
                        'appendContinuationItemsAction']['continuationItems']
                    videos = important_content
                except (KeyError, IndexError, TypeError) as p:
                    logger.info(p)
                    return [], None

        try:
            continuation = videos[-1]['continuationItemRenderer'][
                'continuationEndpoint'
            ]['continuationCommand']['token']
            videos = videos[:-1]
        except (KeyError, IndexError):
            # if there is an error, no continuation is available
            continuation = None

        # remove duplicates
        return (
            uniqueify(
                list(
                    # only extract the video ids from the video data
                    map(
                        lambda x: (
                            f"/watch?v="
                            f"{x['gridVideoRenderer']['videoId']}"
                        ),
                        videos
                    )
                ),
            ),
            continuation,
        )

```

# pytube/contrib/search.py
```python
"""Module for interacting with YouTube search."""
# Native python imports
import logging

# Local imports
from pytube import YouTube
from pytube.innertube import InnerTube


logger = logging.getLogger(__name__)


class Search:
    def __init__(self, query):
        """Initialize Search object.

        :param str query:
            Search query provided by the user.
        """
        self.query = query
        self._innertube_client = InnerTube(client='WEB')

        # The first search, without a continuation, is structured differently
        #  and contains completion suggestions, so we must store this separately
        self._initial_results = None

        self._results = None
        self._completion_suggestions = None

        # Used for keeping track of query continuations so that new results
        #  are always returned when get_next_results() is called
        self._current_continuation = None

    @property
    def completion_suggestions(self):
        """Return query autocompletion suggestions for the query.

        :rtype: list
        :returns:
            A list of autocomplete suggestions provided by YouTube for the query.
        """
        if self._completion_suggestions:
            return self._completion_suggestions
        if self.results:
            self._completion_suggestions = self._initial_results['refinements']
        return self._completion_suggestions

    @property
    def results(self):
        """Return search results.

        On first call, will generate and return the first set of results.
        Additional results can be generated using ``.get_next_results()``.

        :rtype: list
        :returns:
            A list of YouTube objects.
        """
        if self._results:
            return self._results

        videos, continuation = self.fetch_and_parse()
        self._results = videos
        self._current_continuation = continuation
        return self._results

    def get_next_results(self):
        """Use the stored continuation string to fetch the next set of results.

        This method does not return the results, but instead updates the results property.
        """
        if self._current_continuation:
            videos, continuation = self.fetch_and_parse(self._current_continuation)
            self._results.extend(videos)
            self._current_continuation = continuation
        else:
            raise IndexError

    def fetch_and_parse(self, continuation=None):
        """Fetch from the innertube API and parse the results.

        :param str continuation:
            Continuation string for fetching results.
        :rtype: tuple
        :returns:
            A tuple of a list of YouTube objects and a continuation string.
        """
        # Begin by executing the query and identifying the relevant sections
        #  of the results
        raw_results = self.fetch_query(continuation)

        # Initial result is handled by try block, continuations by except block
        try:
            sections = raw_results['contents']['twoColumnSearchResultsRenderer'][
                'primaryContents']['sectionListRenderer']['contents']
        except KeyError:
            sections = raw_results['onResponseReceivedCommands'][0][
                'appendContinuationItemsAction']['continuationItems']
        item_renderer = None
        continuation_renderer = None
        for s in sections:
            if 'itemSectionRenderer' in s:
                item_renderer = s['itemSectionRenderer']
            if 'continuationItemRenderer' in s:
                continuation_renderer = s['continuationItemRenderer']

        # If the continuationItemRenderer doesn't exist, assume no further results
        if continuation_renderer:
            next_continuation = continuation_renderer['continuationEndpoint'][
                'continuationCommand']['token']
        else:
            next_continuation = None

        # If the itemSectionRenderer doesn't exist, assume no results.
        if item_renderer:
            videos = []
            raw_video_list = item_renderer['contents']
            for video_details in raw_video_list:
                # Skip over ads
                if video_details.get('searchPyvRenderer', {}).get('ads', None):
                    continue

                # Skip "recommended" type videos e.g. "people also watched" and "popular X"
                #  that break up the search results
                if 'shelfRenderer' in video_details:
                    continue

                # Skip auto-generated "mix" playlist results
                if 'radioRenderer' in video_details:
                    continue

                # Skip playlist results
                if 'playlistRenderer' in video_details:
                    continue

                # Skip channel results
                if 'channelRenderer' in video_details:
                    continue

                # Skip 'people also searched for' results
                if 'horizontalCardListRenderer' in video_details:
                    continue

                # Can't seem to reproduce, probably related to typo fix suggestions
                if 'didYouMeanRenderer' in video_details:
                    continue

                # Seems to be the renderer used for the image shown on a no results page
                if 'backgroundPromoRenderer' in video_details:
                    continue

                if 'videoRenderer' not in video_details:
                    logger.warning('Unexpected renderer encountered.')
                    logger.warning(f'Renderer name: {video_details.keys()}')
                    logger.warning(f'Search term: {self.query}')
                    logger.warning(
                        'Please open an issue at '
                        'https://github.com/pytube/pytube/issues '
                        'and provide this log output.'
                    )
                    continue

                # Extract relevant video information from the details.
                # Some of this can be used to pre-populate attributes of the
                #  YouTube object.
                vid_renderer = video_details['videoRenderer']
                vid_id = vid_renderer['videoId']
                vid_url = f'https://www.youtube.com/watch?v={vid_id}'
                vid_title = vid_renderer['title']['runs'][0]['text']
                vid_channel_name = vid_renderer['ownerText']['runs'][0]['text']
                vid_channel_uri = vid_renderer['ownerText']['runs'][0][
                    'navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
                # Livestreams have "runs", non-livestreams have "simpleText",
                #  and scheduled releases do not have 'viewCountText'
                if 'viewCountText' in vid_renderer:
                    if 'runs' in vid_renderer['viewCountText']:
                        vid_view_count_text = vid_renderer['viewCountText']['runs'][0]['text']
                    else:
                        vid_view_count_text = vid_renderer['viewCountText']['simpleText']
                    # Strip ' views' text, then remove commas
                    stripped_text = vid_view_count_text.split()[0].replace(',','')
                    if stripped_text == 'No':
                        vid_view_count = 0
                    else:
                        vid_view_count = int(stripped_text)
                else:
                    vid_view_count = 0
                if 'lengthText' in vid_renderer:
                    vid_length = vid_renderer['lengthText']['simpleText']
                else:
                    vid_length = None

                vid_metadata = {
                    'id': vid_id,
                    'url': vid_url,
                    'title': vid_title,
                    'channel_name': vid_channel_name,
                    'channel_url': vid_channel_uri,
                    'view_count': vid_view_count,
                    'length': vid_length
                }

                # Construct YouTube object from metadata and append to results
                vid = YouTube(vid_metadata['url'])
                vid.author = vid_metadata['channel_name']
                vid.title = vid_metadata['title']
                videos.append(vid)
        else:
            videos = None

        return videos, next_continuation

    def fetch_query(self, continuation=None):
        """Fetch raw results from the innertube API.

        :param str continuation:
            Continuation string for fetching results.
        :rtype: dict
        :returns:
            The raw json object returned by the innertube API.
        """
        query_results = self._innertube_client.search(self.query, continuation)
        if not self._initial_results:
            self._initial_results = query_results
        return query_results  # noqa:R504

```

# pytube/contrib/playlist.py
```python
"""Module to download a complete playlist from a youtube channel."""
import json
import logging
from collections.abc import Sequence
from datetime import date, datetime
from typing import Dict, Iterable, List, Optional, Tuple, Union

from pytube import extract, request, YouTube
from pytube.helpers import cache, DeferredGeneratorList, install_proxy, uniqueify

logger = logging.getLogger(__name__)


class Playlist(Sequence):
    """Load a YouTube playlist with URL"""

    def __init__(self, url: str, proxies: Optional[Dict[str, str]] = None):
        if proxies:
            install_proxy(proxies)

        self._input_url = url

        # These need to be initialized as None for the properties.
        self._html = None
        self._ytcfg = None
        self._initial_data = None
        self._sidebar_info = None

        self._playlist_id = None

    @property
    def playlist_id(self):
        """Get the playlist id.

        :rtype: str
        """
        if self._playlist_id:
            return self._playlist_id
        self._playlist_id = extract.playlist_id(self._input_url)
        return self._playlist_id

    @property
    def playlist_url(self):
        """Get the base playlist url.

        :rtype: str
        """
        return f"https://www.youtube.com/playlist?list={self.playlist_id}"

    @property
    def html(self):
        """Get the playlist page html.

        :rtype: str
        """
        if self._html:
            return self._html
        self._html = request.get(self.playlist_url)
        return self._html

    @property
    def ytcfg(self):
        """Extract the ytcfg from the playlist page html.

        :rtype: dict
        """
        if self._ytcfg:
            return self._ytcfg
        self._ytcfg = extract.get_ytcfg(self.html)
        return self._ytcfg

    @property
    def initial_data(self):
        """Extract the initial data from the playlist page html.

        :rtype: dict
        """
        if self._initial_data:
            return self._initial_data
        else:
            self._initial_data = extract.initial_data(self.html)
            return self._initial_data

    @property
    def sidebar_info(self):
        """Extract the sidebar info from the playlist page html.

        :rtype: dict
        """
        if self._sidebar_info:
            return self._sidebar_info
        else:
            self._sidebar_info = self.initial_data['sidebar'][
                'playlistSidebarRenderer']['items']
            return self._sidebar_info

    @property
    def yt_api_key(self):
        """Extract the INNERTUBE_API_KEY from the playlist ytcfg.

        :rtype: str
        """
        return self.ytcfg['INNERTUBE_API_KEY']

    def _paginate(
        self, until_watch_id: Optional[str] = None
    ) -> Iterable[List[str]]:
        """Parse the video links from the page source, yields the /watch?v=
        part from video link

        :param until_watch_id Optional[str]: YouTube Video watch id until
            which the playlist should be read.

        :rtype: Iterable[List[str]]
        :returns: Iterable of lists of YouTube watch ids
        """
        videos_urls, continuation = self._extract_videos(
            json.dumps(extract.initial_data(self.html))
        )
        if until_watch_id:
            try:
                trim_index = videos_urls.index(f"/watch?v={until_watch_id}")
                yield videos_urls[:trim_index]
                return
            except ValueError:
                pass
        yield videos_urls

        # Extraction from a playlist only returns 100 videos at a time
        # if self._extract_videos returns a continuation there are more
        # than 100 songs inside a playlist, so we need to add further requests
        # to gather all of them
        if continuation:
            load_more_url, headers, data = self._build_continuation_url(continuation)
        else:
            load_more_url, headers, data = None, None, None

        while load_more_url and headers and data:  # there is an url found
            logger.debug("load more url: %s", load_more_url)
            # requesting the next page of videos with the url generated from the
            # previous page, needs to be a post
            req = request.post(load_more_url, extra_headers=headers, data=data)
            # extract up to 100 songs from the page loaded
            # returns another continuation if more videos are available
            videos_urls, continuation = self._extract_videos(req)
            if until_watch_id:
                try:
                    trim_index = videos_urls.index(f"/watch?v={until_watch_id}")
                    yield videos_urls[:trim_index]
                    return
                except ValueError:
                    pass
            yield videos_urls

            if continuation:
                load_more_url, headers, data = self._build_continuation_url(
                    continuation
                )
            else:
                load_more_url, headers, data = None, None, None

    def _build_continuation_url(self, continuation: str) -> Tuple[str, dict, dict]:
        """Helper method to build the url and headers required to request
        the next page of videos

        :param str continuation: Continuation extracted from the json response
            of the last page
        :rtype: Tuple[str, dict, dict]
        :returns: Tuple of an url and required headers for the next http
            request
        """
        return (
            (
                # was changed to this format (and post requests)
                # between 2021.03.02 and 2021.03.03
                "https://www.youtube.com/youtubei/v1/browse?key="
                f"{self.yt_api_key}"
            ),
            {
                "X-YouTube-Client-Name": "1",
                "X-YouTube-Client-Version": "2.20200720.00.02",
            },
            # extra data required for post request
            {
                "continuation": continuation,
                "context": {
                    "client": {
                        "clientName": "WEB",
                        "clientVersion": "2.20200720.00.02"
                    }
                }
            }
        )

    @staticmethod
    def _extract_videos(raw_json: str) -> Tuple[List[str], Optional[str]]:
        """Extracts videos from a raw json page

        :param str raw_json: Input json extracted from the page or the last
            server response
        :rtype: Tuple[List[str], Optional[str]]
        :returns: Tuple containing a list of up to 100 video watch ids and
            a continuation token, if more videos are available
        """
        initial_data = json.loads(raw_json)
        try:
            # this is the json tree structure, if the json was extracted from
            # html
            section_contents = initial_data["contents"][
                "twoColumnBrowseResultsRenderer"][
                "tabs"][0]["tabRenderer"]["content"][
                "sectionListRenderer"]["contents"]
            try:
                # Playlist without submenus
                important_content = section_contents[
                    0]["itemSectionRenderer"][
                    "contents"][0]["playlistVideoListRenderer"]
            except (KeyError, IndexError, TypeError):
                # Playlist with submenus
                important_content = section_contents[
                    1]["itemSectionRenderer"][
                    "contents"][0]["playlistVideoListRenderer"]
            videos = important_content["contents"]
        except (KeyError, IndexError, TypeError):
            try:
                # this is the json tree structure, if the json was directly sent
                # by the server in a continuation response
                # no longer a list and no longer has the "response" key
                important_content = initial_data['onResponseReceivedActions'][0][
                    'appendContinuationItemsAction']['continuationItems']
                videos = important_content
            except (KeyError, IndexError, TypeError) as p:
                logger.info(p)
                return [], None

        try:
            continuation = videos[-1]['continuationItemRenderer'][
                'continuationEndpoint'
            ]['continuationCommand']['token']
            videos = videos[:-1]
        except (KeyError, IndexError):
            # if there is an error, no continuation is available
            continuation = None

        # remove duplicates
        return (
            uniqueify(
                list(
                    # only extract the video ids from the video data
                    map(
                        lambda x: (
                            f"/watch?v="
                            f"{x['playlistVideoRenderer']['videoId']}"
                        ),
                        videos
                    )
                ),
            ),
            continuation,
        )

    def trimmed(self, video_id: str) -> Iterable[str]:
        """Retrieve a list of YouTube video URLs trimmed at the given video ID

        i.e. if the playlist has video IDs 1,2,3,4 calling trimmed(3) returns
        [1,2]
        :type video_id: str
            video ID to trim the returned list of playlist URLs at
        :rtype: List[str]
        :returns:
            List of video URLs from the playlist trimmed at the given ID
        """
        for page in self._paginate(until_watch_id=video_id):
            yield from (self._video_url(watch_path) for watch_path in page)

    def url_generator(self):
        """Generator that yields video URLs.

        :Yields: Video URLs
        """
        for page in self._paginate():
            for video in page:
                yield self._video_url(video)

    @property  # type: ignore
    @cache
    def video_urls(self) -> DeferredGeneratorList:
        """Complete links of all the videos in playlist

        :rtype: List[str]
        :returns: List of video URLs
        """
        return DeferredGeneratorList(self.url_generator())

    def videos_generator(self):
        for url in self.video_urls:
            yield YouTube(url)

    @property
    def videos(self) -> Iterable[YouTube]:
        """Yields YouTube objects of videos in this playlist

        :rtype: List[YouTube]
        :returns: List of YouTube
        """
        return DeferredGeneratorList(self.videos_generator())

    def __getitem__(self, i: Union[slice, int]) -> Union[str, List[str]]:
        return self.video_urls[i]

    def __len__(self) -> int:
        return len(self.video_urls)

    def __repr__(self) -> str:
        return f"{repr(self.video_urls)}"

    @property
    @cache
    def last_updated(self) -> Optional[date]:
        """Extract the date that the playlist was last updated.

        For some playlists, this will be a specific date, which is returned as a datetime
        object. For other playlists, this is an estimate such as "1 week ago". Due to the
        fact that this value is returned as a string, pytube does a best-effort parsing
        where possible, and returns the raw string where it is not possible.

        :return: Date of last playlist update where possible, else the string provided
        :rtype: datetime.date
        """
        last_updated_text = self.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer'][
            'stats'][2]['runs'][1]['text']
        try:
            date_components = last_updated_text.split()
            month = date_components[0]
            day = date_components[1].strip(',')
            year = date_components[2]
            return datetime.strptime(
                f"{month} {day:0>2} {year}", "%b %d %Y"
            ).date()
        except (IndexError, KeyError):
            return last_updated_text

    @property
    @cache
    def title(self) -> Optional[str]:
        """Extract playlist title

        :return: playlist title (name)
        :rtype: Optional[str]
        """
        return self.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer'][
            'title']['runs'][0]['text']

    @property
    def description(self) -> str:
        return self.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer'][
            'description']['simpleText']

    @property
    def length(self):
        """Extract the number of videos in the playlist.

        :return: Playlist video count
        :rtype: int
        """
        count_text = self.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer'][
            'stats'][0]['runs'][0]['text']
        count_text = count_text.replace(',','')
        return int(count_text)

    @property
    def views(self):
        """Extract view count for playlist.

        :return: Playlist view count
        :rtype: int
        """
        # "1,234,567 views"
        views_text = self.sidebar_info[0]['playlistSidebarPrimaryInfoRenderer'][
            'stats'][1]['simpleText']
        # "1,234,567"
        count_text = views_text.split()[0]
        # "1234567"
        count_text = count_text.replace(',', '')
        return int(count_text)

    @property
    def owner(self):
        """Extract the owner of the playlist.

        :return: Playlist owner name.
        :rtype: str
        """
        return self.sidebar_info[1]['playlistSidebarSecondaryInfoRenderer'][
            'videoOwner']['videoOwnerRenderer']['title']['runs'][0]['text']

    @property
    def owner_id(self):
        """Extract the channel_id of the owner of the playlist.

        :return: Playlist owner's channel ID.
        :rtype: str
        """
        return self.sidebar_info[1]['playlistSidebarSecondaryInfoRenderer'][
            'videoOwner']['videoOwnerRenderer']['title']['runs'][0][
            'navigationEndpoint']['browseEndpoint']['browseId']

    @property
    def owner_url(self):
        """Create the channel url of the owner of the playlist.

        :return: Playlist owner's channel url.
        :rtype: str
        """
        return f'https://www.youtube.com/channel/{self.owner_id}'

    @staticmethod
    def _video_url(watch_path: str):
        return f"https://www.youtube.com{watch_path}"

```

