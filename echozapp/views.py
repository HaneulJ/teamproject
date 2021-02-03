from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request) :
    template = loader.get_template('index.html')
    return HttpResponse(template.render(None, request))

def about(request) :
    template = loader.get_template('about.html')
    return HttpResponse(template.render(None, request))

def categories(request) :
    template = loader.get_template('categories.html')
    return HttpResponse(template.render(None, request))

def contact(request) :
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(None, request))

def blogSingle(request) :
    template = loader.get_template('blog-single.html')
    return HttpResponse(template.render(None, request))

# Create your views here.
