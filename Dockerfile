FROM nginx:1.21-alpine3.11-slim021

# Copy everything in the current working directory to the default nginx folder
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP traffic
EXPOSE 8000

# Add a volume to persist data
VOLUME /usr/share/nginx/html021
