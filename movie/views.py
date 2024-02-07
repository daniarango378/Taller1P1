from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    #return HttpResponse('<H1>Welcome to homepage</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Greg Lim'})