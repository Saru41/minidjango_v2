Django models
A model is the single, definitive source of information about your data.
In short model class is your DDL
django database
django uses sqlite3 as default database (shipped along with django)
sqlite3 is lightweight database and it is called as in-memory database
sqlite3 is typically used for development (not for production)
If we want to change default database in django...
We go to settings.py file and update DB engine
TODO refer - https://docs.djangoproject.com/en/4.1/ref/databases/#mysql-notes
migrations
When you add any new table OR alter any existing table...
python manage.py makemigrations (detection)
python manage.py migrate (apply)
ORM (Object Relational Mapper)
Flexibility
models
In django models, id field is auto-created.
how to install sqlite3 command line client on my windows machine?
how to access interactive shell in django?
In order to access your database entries in ORM way, django has provided a tool called shell

python manage.py shell

HOW TO capture all the entries in django model?

    >>> from jobs.models import Portal
    >>> # ORM query to get all the enties in `Portal` Table
    >>> Portal.objects.all()
    <QuerySet [<Portal: Portal object (1)>, <Portal: Portal object (2)>]>
    >>>
ORM query to create new entry in table
>>> Portal.objects.create()
<Portal: Portal object (3)>
>>> Portal.objects.create(name="glassdoor.com", description="company review website")
<Portal: Portal object (4)>
>>> Portal.objects.create(name="findjob.com", description="random job website")
<Portal: Portal object (5)>
How to get a particular portal based on primary key?
>>> Portal.objects.get(pk=1)
<Portal: portal - Naukri.com>
>>> Portal.objects.get(id=1)
<Portal: portal - Naukri.com>
How to filter a particular set of portals based on name?
>>> Portal.objects.filter(name="naukri.com")
<QuerySet []>
>>> Portal.objects.filter(name="Naukri.com")
<QuerySet [<Portal: portal - Naukri.com>]>
>>> result = Portal.objects.filter(name="Naukri.com")
>>> result[0]
<Portal: portal - Naukri.com>
how to delete portal?
>>> portal_obj = Portal.objects.get(pk=2)
>>> portal_obj
<Portal: 2 portal - linkedin.com>
>>> portal_obj.delete()
(1, {'jobs.Portal': 1})
What is shortcut to get a record from certain DB table using Django-ORM using primary key (when primary key column name is not known)?
Portal.objects.get(pk=1)