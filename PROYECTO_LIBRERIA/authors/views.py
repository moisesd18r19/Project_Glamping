from django.shortcuts import render

def authors (request):
    return render (request, 'authors/index.html')

# Create your views here.
