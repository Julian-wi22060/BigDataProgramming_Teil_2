FROM nginx:latest

# Remove the standard-nginx-configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy the user defined nginx.conf into the container-directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080
EXPOSE 8080

# Starten Sie den Nginx-Server
CMD ["nginx", "-g", "daemon off;"]
