from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "one/index.html")

def resume(request):
    return render(request, "one/resume.html")

def projects(request):
    return render(request, "one/projects.html")

def contact(request):
    return render(request, "one/contact.html")