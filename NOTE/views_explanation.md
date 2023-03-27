how to create new application and add a function based view under it?
django-admin startapp <app-name>
OR python manage.py startapp <app-name>
when you create new application you get views.py file auto-created under application
we write django function based views like following -
from django.shortcuts import HttpResponse, render

def view_name(request):
    return render(request, "subapp/welcome.html")
what is django working directory?
what is django project root?
wherever you have manage.py file