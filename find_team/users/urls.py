from django.urls import path
from .views import profile_view, RegisterView, UsersPasswordResetView, UsersPasswordResetDoneView, \
    UsersPasswordChangeView, UsersPasswordChangeDoneView, answer_view

app_name = 'users'
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path("password_reset/", UsersPasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", UsersPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password_change/", UsersPasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", UsersPasswordChangeDoneView.as_view(), name="password_change_done"),
    path('profile/answer/<int:pk>', answer_view, name='answer'),
]
