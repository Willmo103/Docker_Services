# Use the .NET SDK image with git
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env

# Install git
RUN apt-get update && apt-get install -y git

# Set the working directory
WORKDIR /app

# Clone the specific repository
RUN git clone https://github.com/Willmo103/FlattenCodeBase.git .

# Restore dependencies
RUN dotnet restore

# Build the application
RUN dotnet build -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/runtime:8.0
WORKDIR /app
COPY --from=build-env /app/out .

# Install git in the runtime image
RUN apt-get update && apt-get install -y git

# Copy the entry point script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entry point
ENTRYPOINT ["/entrypoint.sh"]
