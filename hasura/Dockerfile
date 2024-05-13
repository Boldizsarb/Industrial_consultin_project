FROM hasura/graphql-engine:v2.38.0

# Install Hasura CLI
RUN apt-get update && apt-get install -y curl
RUN curl -L https://github.com/hasura/graphql-engine/raw/stable/cli/get.sh | bash

# Copy your scripts and metadata JSON
COPY hasura-entrypoint.sh /hasura-entrypoint.sh
COPY hasura_metadata.json /hasura_metadata.json

# Make the entry script executable
RUN chmod +x /hasura-entrypoint.sh

ENTRYPOINT ["/hasura-entrypoint.sh"]
