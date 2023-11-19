from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('create/', views.team_create, name='create')
]
