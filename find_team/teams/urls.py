from django.urls import path
from . import views
from .views import TeamDetailView, TeamUpdateView, TeamDeleteView

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('create/', views.team_create, name='create'),
    path('<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('<int:pk>/update', TeamUpdateView.as_view(), name='team_update'),
    path('<int:pk>/delete', TeamDeleteView.as_view(), name='team_delete'),
]
