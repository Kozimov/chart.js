from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from .models import Country, Post

def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'index.html', context)

def example(request):
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, 'example.html', context)

def pieChart(request):
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, 'pieChart.html', context)