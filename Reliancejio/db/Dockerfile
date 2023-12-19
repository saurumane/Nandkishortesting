FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=python8
ENV MYSQL_USER=MYSQL_ROOT_PASSWORD
ENV MYSQL_PASSWORD=root

# Copy the database initialization script
COPY init.sql /docker-entrypoint-initdb.d/
