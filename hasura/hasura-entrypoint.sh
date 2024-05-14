#!/bin/bash

# Wait for PostgreSQL to start
until nc -z industrial-consulting-postgresql 5432; do
  echo "Waiting for PostgreSQL to start..."
  sleep 1
done

# Start Hasura GraphQL engine in the background
graphql-engine serve --enable-console &

# Wait for Hasura to start
sleep 10

# Initialize Hasura project directory
hasura init --directory /hasura-project

# Change to the Hasura project directory
cd /hasura-project

# Print current directory and list files (for debugging)
echo "Current directory: $(pwd)"
echo "Files in the directory: $(ls)"

# Export Hasura metadata
echo "Exporting Hasura metadata..."
hasura metadata export

# Apply Hasura metadata changes
echo "Applying Hasura metadata..."
hasura metadata apply

echo "Hasura metadata updated successfully"
echo "Current directory: $(pwd)"
echo "Files in the directory: $(ls)"
cd ..
cp -R /hasura-project/. /hasura

# Wait for Hasura GraphQL engine to exit
wait