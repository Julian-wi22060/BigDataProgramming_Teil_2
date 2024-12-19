FROM nginx:latest

# Copy the nginx.conf into the container-directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080
EXPOSE 8080

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
