Slot-Checker-using-Django-and-Ajax
====================
A Web Application to book slots for trial class of an E-learning Platform. The project is made using Django and Ajax. 
Users can book slot of their classes based on available slots created by admin. The project also applies to all the system that provides slot booking features be it a Hotel Room booking, Exams Slot booking e.t.c. 

## Installation
Use Python 3 (recommended v3.6)

Git clone then use a virtual environment.

Make migrations.
```sh
python manage.py makemigrations
python manage.py migrate
```

Create superuser.
```sh
python manage.py createsuperuser
```

Start server.
```sh
python manage.py runserver
```

