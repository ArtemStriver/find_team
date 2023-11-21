from django.urls import path
from .views import profile_view, RegisterView

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
]
