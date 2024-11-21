from django.urls import  path
from . import views


urlpatterns = [
    path('', views.mainapp, name='home'),
    path('about/', views.aboutapp, name='about'),
    path('programs/', views.programsapp, name='programs'),
    path('platform/', views.platformapp, name='platform'),
]