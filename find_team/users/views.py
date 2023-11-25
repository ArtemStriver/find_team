from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordChangeDoneView, \
    PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import RegisterForm, AnswerForm
from teams import models
from .models import Answer


@login_required
def profile_view(request):
    """Представление профиля пользователя."""
    my_letters = models.JoinInTeam.objects.filter(author=request.user.id).order_by('-id')
    my_teams = models.Teams.objects.filter(owner_id=request.user.id).order_by('-id')
    massages = models.JoinInTeam.objects.all()  # filter(team_boss=my_teams.id)
    answers = Answer.objects.filter(answer_recipient=request.user.id).order_by('-id')

    data = {
        'my_letters': my_letters,
        'my_teams': my_teams,
        'massages': massages,
        'answers': answers,
    }

    return render(request, 'users/profile.html', data)


@login_required
def answer_view(request, pk):
    """Представление ответов на заявки пользователя."""
    error = ''
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            author_id = models.JoinInTeam.objects.get(id=pk)
            form = form.save(commit=False)
            form.answer_author = request.user
            form.answer_recipient = author_id.author_id
            form.save()
            # join_in = models.JoinInTeam.objects.get(id=pk)
            author_id.delete()
            return redirect('users:profile')
        else:
            error = 'Форма заполнена неверно.'

    form = AnswerForm()

    data = {
        'pk': pk,
        'form': form,
        'error': error
    }

    return render(request, 'users/answer_form.html', data)


def delete_join(request, pk):
    """Функция удаления входящей заявки."""
    join_in = models.JoinInTeam.objects.get(id=pk)
    join_in.delete()
    return HttpResponseRedirect('/users/profile')


def delete_answer(request, pk):
    """Функция удаления ответа на заявку."""
    answer = Answer.objects.get(id=pk)
    answer.delete()
    return HttpResponseRedirect('/users/profile')


class RegisterView(FormView):
    """Представление формы регистрации пользователя."""
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/users/profile'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UsersPasswordResetView(PasswordResetView):
    """Представление сброса пароля пользователя."""
    template_name = 'users/password_reset_email.html'


class UsersPasswordResetDoneView(PasswordResetDoneView):
    """Представление после сброса пароля пользователя."""
    template_name = 'users/password_reset_done.html'


class UsersPasswordChangeView(PasswordChangeView):
    """Представление изменения пароля пользователя."""
    template_name = 'users/password_change.html'


class UsersPasswordChangeDoneView(PasswordChangeDoneView):
    """Представление после изменения пароля пользователя."""
    template_name = 'users/password_change_done.html'
