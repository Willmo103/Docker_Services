#!/bin/bash

# Check if a Git URL is provided
if [ $# -eq 0 ]; then
    echo "Please provide a Git repository URL"
    exit 1
fi

# Clone the repository
git clone $1 /tmp/repo

# Set up compression flag
COMPRESS_FLAG=""
if [ "$COMPRESS" = "true" ]; then
    COMPRESS_FLAG="-c"
fi

# Run the CodeFlattener
dotnet /app/CodeFlattener.dll /tmp/repo /app/output.md $COMPRESS_FLAG

# Check if the output file was created
if [ -f /app/output.md ]; then
    echo "Repository flattened successfully. Output saved to /app/output.md"
    if [ "$COMPRESS" = "true" ]; then
        echo "Compression was applied."
    fi
else
    echo "Failed to flatten the repository"
    exit 1
fi
