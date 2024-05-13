FROM hasura/graphql-engine:v2.16.1.cli-migrations-v3

# Install necessary tools
RUN apt-get update && apt-get install -y curl netcat

# Copy migrations and metadata directories
COPY ./metadata ./metadata

# Set the entrypoint
ENTRYPOINT ["graphql-engine"]

# Set the default command
CMD ["serve", "--enable-console"]