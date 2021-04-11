from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def Blog_Dashboard(request):
    return render(request, "Blog_Dashboard.html")

def Tables(request):
    return render(request, "Tables.html")

def User_Profile(request):
    return render(request, "User_Profile.html")

def Forms_And_Components(request):
    return render(request, "Forms_And_Components.html")

def Errors(request):
    return render(request, "Errors.html")

def Blog_Posts(request):
    return render(request, "Blog_Posts.html")

def Add_New_Posts(request):
    return render(request, "Add_New_Posts.html")
