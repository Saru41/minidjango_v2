django-admin startproject <project-name>
python manage.py runserver
Go to home-url, you will see default django welcome page
django-admin startapp app1
The only relative endpoint available at this stage is /admin
You cannot yet access admin page because admin is a application configured in settings.py
There are some pre-installed apps whenever we creat django project
For example django.contrib.admin is one of them
To access these projects we need to makemigrations & migrate first.
python manage.py makemigrations (detects changes related to application models)
python manage.py migrate (applies model changes to database)
Now you can access admin page, but you don't have application user yet.
python manage.py createsuperuser
I can log into admin interface using user created in above step.
You can now write new views in views.py file under application
We do URL binding of this view by adding URL mapping in urls.py file
We also need to register any new application that we create in settings.py