from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/users/profile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UsersPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset_email.html'


class UsersPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
