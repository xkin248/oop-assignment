#!/bin/bash

# Check if MySQL is installed
if ! command -v mysql >/dev/null 2>&1; then
    echo "MySQL is not installed. Installing MySQL server..."

    # Install MySQL (for Debian/Ubuntu)
    sudo apt update
    sudo DEBIAN_FRONTEND=noninteractive apt install -y mysql-server

    echo "MySQL installed."
    sudo systemctl start mysql
    echo "MySQL service started."

    # Set root password to 'hello'
    echo "Setting root password to 'hello'..."
    sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hello'; FLUSH PRIVILEGES;"
    echo "Root password set to 'hello'."

else
    echo "MySQL is already installed."

    # Start MySQL service if not running
    if ! pgrep -x "mysqld" > /dev/null; then
        echo "Starting MySQL service..."
        sudo systemctl start mysql
    fi

    # Change password just in case
    echo "Ensuring root password is set to 'hello'..."
    sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hello'; FLUSH PRIVILEGES;"
fi

# Optional Docker fallback
echo "Do you want to run MySQL in Docker instead? (y/n)"
read run_docker

if [ "$run_docker" == "y" ]; then
    echo "Starting MySQL in Docker..."
    docker run --name mysql-dev -e MYSQL_ROOT_PASSWORD=hello -p 3306:3306 -d mysql:8
    echo "Docker container started. You can connect via: mysql -h 127.0.0.1 -P 3306 -u root -p"
fi

