# usersManagement

## setup (under Ubuntu):
install virtualenv and mysql-server:
```
sudo apt install virtualenv mysql-server
```
clone the repo:
```
git clone https://github.com/oz-elhassid/usersManagement
cd usersManagement
```
activate virtualenv:
```
virtualenv ./venv/ -p python3.6
source ./venv/bin/activate
```
install the dependencies:
```
pip install -r requirements.txt
```
start mysql:
```
sudo /etc/init.d/mysql start
```
and through the mysql shell create a user to work with:
```
sudo mysql
CREATE USER 'oz'@'localhost' IDENTIFIED BY '1234';
```
create a database to work with, grant permissions and quit the mysql shell:
```
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON mydatabase.* TO 'oz'@'localhost';
quit
```
migrate changes to the database:
```
python manage.py migrate
```
create an admin (follow the on-screen-instructions):
```
python manage.py createsuperuser
```
finaly, run the server:
```
python manage.py runserver
```
