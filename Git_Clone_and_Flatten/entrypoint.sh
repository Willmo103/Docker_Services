#!/bin/bash

# Check if a Git URL is provided
if [ $# -eq 0 ]; then
    echo "Please provide a Git repository URL"
    exit 1
fi

# Clone the repository
git clone $1 /tmp/repo

# Get the repository name
REPO_NAME=$(basename -s .git $(echo $1 | sed 's/\/$//'))

# Set up compression flag
COMPRESS_FLAG=""
if [ "$COMPRESS" = "true" ]; then
    COMPRESS_FLAG="-c"
fi

# Make sure CodeFlattener is executable
chmod +x /app/CodeFlattener

# Run the CodeFlattener
/app/CodeFlattener /tmp/repo /output/${REPO_NAME}.md $COMPRESS_FLAG

# Check if the output file was created
if [ -f /output/${REPO_NAME}.md ]; then
    echo "Repository flattened successfully. Output saved to /output/${REPO_NAME}.md"
    if [ "$COMPRESS" = "true" ]; then
        echo "Compression was applied."
    fi
else
    echo "Failed to flatten the repository"
    exit 1
fi
