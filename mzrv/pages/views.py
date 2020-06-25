from django.shortcuts import render

from games.models import Games


def index(request):
    games = Games.objects.all()[:3]

    extra_context = {
        'page': 'Jogos',
        'games': games,
        'consoles': [],
        'acessories': []
    }
    return render(request, 'pages/index.html', extra_context)

def games(request):
    games = Games.objects.all().order_by('name')

    extra_context = {
        'page': 'Jogos',
        'objects': games
    }
    return render(request, 'pages/listings.html', extra_context)

def consoles(request):
    extra_context = {
        'page': 'Consoles',
        'objects': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'PlayStation 4 1TB',
                'price': '1899.99',
            }
        ]
    }
    return render(request, 'pages/listings.html', extra_context)

def acessories(request):
    extra_context = {
        'page': 'Acessórios',
        'objects': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Controle Dualshock 4 - PlayStation 4 - Preto',
                'price': '159.99',
            }
        ]
    }
    return render(request, 'pages/listings.html', extra_context)
