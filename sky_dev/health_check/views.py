from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'health_check/home_page.html')
def vote(request):
    return render(request, 'health_check/vote_page.html')

#from project template folder

def navbar(request):
    return render (request, 'navbar.html')