from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordChangeDoneView, \
    PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm, AnswerForm
from teams import models
from .models import Answer


@login_required
def profile_view(request):
    my_letters = models.JoinInTeam.objects.filter(author=request.user.id)
    my_teams = models.Teams.objects.filter(owner_id=request.user.id)
    massages = models.JoinInTeam.objects.all() # filter(team_boss=my_teams.id)
    answers = Answer.objects.filter(answer_recipient=request.user.id)

    data = {
        'my_letters': my_letters,
        'my_teams': my_teams,
        'massages': massages,
        'answers': answers,
    }

    return render(request, 'users/profile.html', data)


@login_required
def answer_view(request, pk):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        print('111111')
        if form.is_valid():
            author_id = models.JoinInTeam.objects.get(id=pk)
            print('22222222', author_id)
            form = form.save(commit=False)
            form.answer_author = request.user
            form.answer_recipient = author_id.author_id
            form.save()
            return redirect('users:profile')
        else:
            error = 'Форма заполнена неверно.' # TODO

    form = AnswerForm()

    data = {
        'form': form
    }

    return render(request, 'users/answer_form.html', data)


# class AnswerView(DeleteView):
#     model = Teams
#     success_url = '/teams'
#     template_name = 'teams/team_delete.html'


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


class UsersPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'


class UsersPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'
