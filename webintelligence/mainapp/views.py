from django.shortcuts import render
from django.http import HttpResponse

def mainapp(request):
    return render(request, 'mainapp/main.html')

def aboutapp(request):
    return render(request, 'mainapp/about.html')

def programsapp(request):
    return render(request, 'mainapp/programs.html')

def platformapp(request):
    return render(request, 'mainapp/platform.html')