先install setup_mysql.sh
chmod +x setup_mysql.sh
/workspaces/oop-assignment/mysql/setup_mysql.sh

再 run database.sql
sudo service mysql start
mysql -u root -p < /workspaces/oop-assignment/mysql/databases.sh

run install.sh 如果有 requirements.txt 就不用run
但是要run下面的
cd 'python'
pip install -r requirements.txt