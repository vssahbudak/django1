from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request,'Events/list.html')

def detail(request):
    return render (request,'Events/detail.html')

def search(request):
    return render (request,'Events/search.html')
