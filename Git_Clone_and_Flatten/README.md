# CodeFlattener Docker Image

This Docker image contains the CodeFlattener tool, which flattens and formats code from a Git repository into a single formatted Markdown file.

## Features

- Clones a specified Git repository
- Flattens the code structure into a single file
- Outputs the result as a formatted Markdown file
- Optional compression of the output

## Usage

To use this Docker image, you need to have Docker installed on your system.

### Pull the image

```bash
docker pull willmo103e/codeflattener
```

### Run the container

```bash
docker run -v $(pwd)/output:/app willmo103e/codeflattener https://github.com/user/repo.git
```

This command does the following:

- Mounts the `./output` directory on your host to `/app` in the container
- Clones the specified Git repository
- Flattens the code using CodeFlattener
- Saves the output as `output.md` in the mounted volume

### Using compression

To use the compression feature, run:

```bash
docker run -v $(pwd)/output:/app -e COMPRESS=true willmo103e/codeflattener https://github.com/user/repo.git
```

## Output

The flattened and formatted code will be saved as `output.md` in the directory you mounted to the container.

## Building the image

If you want to build the image yourself:

1. Clone this repository
2. Navigate to the directory containing the Dockerfile
3. Run:

   ```bash
   docker build -t codeflattener .
   ```
