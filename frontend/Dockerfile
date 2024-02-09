# Build stage
FROM node:18 AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install all dependencies, including devDependencies necessary for the build
RUN npm install

# Copy the rest of the frontend codebase into the image
COPY . .

# Build the project using vue-cli-service
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy built assets from build stage to nginx server
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx and keep it running in the foreground
CMD ["nginx", "-g", "daemon off;"]
