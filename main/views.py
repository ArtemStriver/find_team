from django.shortcuts import render


def index(request):
    """Представление главной страницы."""
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    """Представление страницы с информацией о проекте."""
    data = {
        'title': 'О проекте',
    }
    return render(request, 'main/about.html', data)
