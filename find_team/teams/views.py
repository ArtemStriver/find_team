from django.shortcuts import render, redirect
from .models import Teams
from .forms import TeamsForm


def team_list(request):
    teams = Teams.objects.order_by('deadline')
    return render(request, 'teams/team_list.html', {'teams': teams})


def team_create(request):
    error = ''
    if request.method == "POST":
        form = TeamsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list') # TODO доюавить перенаправление на страницу гедактирования заявки
        else:
            error = 'Форма заполнена неверно.'


    form = TeamsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'teams/team_create.html', data)


def team_delete(request):
    pass
