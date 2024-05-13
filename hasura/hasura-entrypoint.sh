#!/bin/bash

# Wait for the database service to be ready
echo "Waiting for the database to be ready..."
if ! nc -z industrial-consulting-postgresql 5432; then
    echo "Database is not ready. Waiting..."
    sleep 5
fi
echo "Database is ready."

echo "Checking if Hasura is ready..."
if ! nc -z industrial-consulting-hasura 8080; then
    echo "Hasura is not ready. Waiting..."
    sleep 5
fi
echo "Hasura is ready."

echo "Checking if Hasura is fully operational..."
if ! curl --output /dev/null --silent --head --fail http://industrial-consulting-hasura:8080/healthz; then
    echo "Hasura is not fully operational. Waiting..."
    sleep 5
fi
echo "Hasura is fully operational."

# Apply metadata
echo "Applying Hasura metadata..."
mkdir -p /hasura-metadata
cp /hasura_metadata.json /hasura-metadata/
hasura metadata apply --endpoint http://industrial-consulting-hasura:8080 --admin-secret postegres --metadata-dir /hasura-metadata --log-level debug

# Start the Hasura GraphQL engine
echo "Starting Hasura GraphQL engine..."
graphql-engine serve