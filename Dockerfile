FROM nginx:1.24-alpine3.17-slim

# Copy everything in the current working directory to the default nginx folder
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Add a volume to persist data
VOLUME /usr/share/nginx/html
