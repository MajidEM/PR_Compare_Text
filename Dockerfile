FROM nginx:1.21-alpine3.10-slim

# Copy everything in the current working directory to the default nginx folder
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Add a volume to persist data
VOLUME /usr/share/nginx/html
