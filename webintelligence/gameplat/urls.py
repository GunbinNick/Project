from django.urls import  path
from . import views

app_name = 'gameplat'

urlpatterns = [
    path('numgame/', views.numsgameapp, name='numgame'),
    path('alphgame/', views.alphgameapp, name='alphgame'),
]