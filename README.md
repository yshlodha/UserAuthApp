# UserAuthApp
Application Which uses email address for authentication in django with feature of multiple email address and primary email is used to login.


##### Configure Your machine with PostgresSQL and MySQL


- This is the link to install (MySQL)[https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/]

Don't forget to configure MySQL with proper user permission.

##### Create Database on MySQL

*In Terminal*

> mysql -u <user> -p

*this will prompt for password enter the valid password for user.*

mysql console will open:

> CREATE DATABASE user_auth;

exits from MySQL.

##### Virtualenv Configuration

Install virtualenv by following instructions if already not exists in your machine: (Virtualenv)[https://virtualenv.pypa.io/en/stable/installation/]

-Note the I have used python3.5 it's upto which python 3 version you want to but recommended is python3.5.

*In terminal*

> virtualenv -p python3.5 env

> cd env/

> source bin/activate

> cd ..


##### Clone app from github

> git clone https://github.com/yshlodha/UserAuthApp.git

> cd UserAuthApp/

> pip install -r requirements.txt


##### Make Settings file according to Your Host Configuration

> cd user_custom_auth/

> open settings.py

Edit DATABASES settings For USER, PASSWORD, HOST, And PORT

> Modifiy this variable as per your database username and password and host and port your dbs running on.

> cd ..

> ls

and see if mamange.py is in the directory if it is you are in correct directory.

##### Run Migrations

> python manage.py migrate


##### Run server

> python manage.py runserver


##### Perform User Creation

go to localhost:8000/singup


