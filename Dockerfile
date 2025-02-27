FROM nginx:1.25-alpine3.17-slim

# Copy everything in the current working directory to the default nginx folder
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 8004

# Add a volume to persist data
VOLUME /usr/share/nginx/html021
