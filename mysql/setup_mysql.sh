#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install MySQL Server
echo "Installing MySQL Server..."
sudo apt install -y mysql-server

# Stop the MySQL service
echo "Stopping MySQL service..."
sudo service mysql stop

# Start MySQL in safe mode
echo "Starting MySQL in safe mode..."
sudo mysqld_safe --skip-grant-tables > /dev/null 2>&1 &

# Wait for MySQL to start
echo "Waiting for MySQL to start in safe mode..."
sleep 5

# Reset the MySQL root password
echo "Resetting MySQL root password to 'hello'..."
mysql -u root <<EOF
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hello';
FLUSH PRIVILEGES;
EOF

# Kill the safe mode process
echo "Stopping MySQL safe mode..."
sudo killall mysqld_safe
sudo killall mysqld

# Restart the MySQL service
echo "Restarting MySQL service..."
sudo service mysql start

echo "MySQL root password has been reset to 'hello'."