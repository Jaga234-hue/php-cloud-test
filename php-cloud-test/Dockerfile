# Use an official PHP image
FROM php:8.2-cli

# Set working directory
WORKDIR /app

# Copy files into container
COPY . /app

# Expose the port Render will use
EXPOSE 10000

# Start PHP's built-in web server
CMD ["php", "-S", "0.0.0.0:10000", "server.php"]
