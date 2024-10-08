FROM nginx:latest

# Write hello world message
RUN echo 'Hello World Bhawesh!' > /usr/share/nginx/html/index.html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
