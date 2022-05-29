from django.shortcuts import render
import datetime as dt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def search(request):
    return render(request, 'search.html')