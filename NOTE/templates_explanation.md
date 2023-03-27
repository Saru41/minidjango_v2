https://jinja.palletsprojects.com/en/3.1.x/templates/#list-of-control-structures

If we follow default template structure in django...
we have to create a folder called templates under django application
Under templates folder we follow convention to create another folder with app name
We create html files under templates/app
The html files rendered with django.shorcuts.render function follow jinja templating
In django.shorcuts.render function we pass dynamic data attributes in the form of dictionary
For example -
def welcome(request):

    cricketers = ["virat", "dhoni", "rahul", "sachin"]

    return render(
        request,
        "jobs/welcome.html",
        {"message": "Good morning", "cricketers": cricketers}
    )
<!DOCTYPE html>
<html lang="en">

<body>

<h1>{{message}}, welcome to this application</h1>
<h2>Here is the list of cricketers</h2>

{% for item in cricketers %}
        <li>{{item}}</li>
{% endfor %}

</body>
</html>