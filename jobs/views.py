from django.shortcuts import render, HttpResponse


# Create your views here.
def welcome(request):
    cricketers = ["virat", "dhoni", "rahul", "sachin"]

    return render(
        request,
        "jobs/welcome.html",
        {"message": "Good morning", "cricketers": cricketers},
    )
