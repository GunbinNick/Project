from django.shortcuts import render
from django.http import HttpResponse

def alphgameapp(request):
    return render(request, 'alphtemp.html')

def numsgameapp(request):
    return render(request, 'numtemp.html')