# fileserver
Simple anonymous fileserver written in Python with Django. 
File upload and download. Access to a file by a unique-generated link.
Using Python 3.5.2 and Django 1.10.4

#installation
```bash 
$ git clone https://github.com/sandpiturtle/fileserver.git 
$ cd fileserver 
$ virtualenv --python=python3 myvenv
$ source myvenv/bin/activate
(myvenv) $ pip install django
(myvenv) $ python manage.py migrate
(myvenv) $ python manage.py runserver
```
