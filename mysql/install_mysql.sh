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

# Secure MySQL Installation
echo "Securing MySQL installation..."
sudo mysql_secure_installation

# Create Database and Tables
echo "Setting up the database..."
mysql -u root -p < /workspaces/oop-assignment/mysql/database.sql

echo "MySQL installation and setup completed successfully!"