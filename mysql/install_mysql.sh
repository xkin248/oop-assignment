#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install MySQL Server
echo "Installing MySQL Server..."
sudo apt install -y mysql-server

# Start MySQL Service
echo "Starting MySQL service..."
sudo service mysql start

# Set MySQL root password to 'hello' and secure installation
echo "Setting MySQL root password and securing installation..."
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hello';"
sudo mysql -e "FLUSH PRIVILEGES;"

# Create Database and Tables
echo "Setting up the database..."
mysql -u root -phello < /workspaces/oop-assignment/mysql/database.sql

echo "MySQL installation and setup completed successfully!"