# usersManagement

## setup:
```
cd ~/usersManagement/
virtualenv ./venv/ -p python3.6
source ./venv/bin/activate
pip install -r requirements.txt
sudo /etc/init.d/mysql start
sudo mysql
CREATE USER 'oz'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON * . * TO 'oz'@'localhost';
quit
python manage.py createsuperuser
python manage.py runserver
```
