from django.shortcuts import render, redirect
from .models import Teams
from .forms import TeamsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def team_list(request):
    teams = Teams.objects.order_by('deadline')
    return render(request, 'teams/team_list.html', {'teams': teams})


class TeamDetailView(DetailView):
    model = Teams
    template_name = 'teams/team_detail.html'
    context_object_name = 'team_detail_view'


class TeamUpdateView(UpdateView):
    model = Teams
    template_name = 'teams/team_create.html'

    form_class = TeamsForm


class TeamDeleteView(DeleteView):
    model = Teams
    success_url = '/teams'
    template_name = 'teams/team_delete.html'


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
