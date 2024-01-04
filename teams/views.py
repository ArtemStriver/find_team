from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Teams
from .forms import TeamsForm, JoinForm
from django.views.generic import DetailView, UpdateView, DeleteView


def team_list(request):
    """Представление списка команд."""
    teams = Teams.objects.order_by('deadline')
    return render(request, 'teams/team_list.html', {'teams': teams})


class TeamDetailView(DetailView):
    """Представление одной команд."""
    model = Teams
    template_name = 'teams/team_detail.html'
    context_object_name = 'team_detail_view'


@login_required
def team_join_in(request, pk):
    """Представление для заявки на вступление в команду."""
    error = ''
    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.team_boss = Teams.objects.get(id=pk)
            form.title = Teams.objects.filter(id=pk).get().title
            form.save()
            return redirect('team_list')
        else:
            error = 'Форма заполнена неверно.'

    form = JoinForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'teams/team_join_in.html', data)


class TeamUpdateView(UpdateView):
    """Представление для обновления команды."""
    model = Teams
    template_name = 'teams/team_create.html'

    form_class = TeamsForm


class TeamDeleteView(DeleteView):
    """Представление для удаления команды."""
    model = Teams
    success_url = '/teams'
    template_name = 'teams/team_delete.html'


@login_required
def team_create(request):
    """Представление для создания команды."""
    error = ''
    if request.method == "POST":
        form = TeamsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('team_list')
        else:
            error = 'Форма заполнена неверно.'

    form = TeamsForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'teams/team_create.html', data)
