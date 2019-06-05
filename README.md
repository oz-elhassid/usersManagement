# usersManagement

## setup:
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
start mysql and create a user to work with:
```
sudo /etc/init.d/mysql start
sudo mysql
CREATE USER 'oz'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON * . * TO 'oz'@'localhost';
quit
```
create an admin (follow the on-screen-instructions):
```
python manage.py createsuperuser
```
finaly, run the server:
```
python manage.py runserver
```
