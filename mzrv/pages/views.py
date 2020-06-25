from django.shortcuts import render

from accessories.models import Accessories
from consoles.models import Consoles
from games.models import Games


def index(request):
    accessories = Accessories.objects.all().order_by('-created_at')[:3]
    consoles = Consoles.objects.all().order_by('-created_at')[:3]
    games = Games.objects.all().order_by('-created_at')[:3]

    extra_context = {
        'page': 'Jogos',
        'games': games,
        'consoles': consoles,
        'accessories': accessories
    }
    return render(request, 'pages/index.html', extra_context)

def games(request):
    games = Games.objects.all()

    extra_context = {
        'page': 'Jogos',
        'objects': games
    }
    return render(request, 'pages/listings.html', extra_context)

def consoles(request):
    consoles = Consoles.objects.all()

    extra_context = {
        'page': 'Videogames',
        'objects': consoles
    }
    return render(request, 'pages/listings.html', extra_context)

def accessories(request):
    accessories = Accessories.objects.all()

    extra_context = {
        'page': 'Acessórios',
        'objects': accessories
    }
    return render(request, 'pages/listings.html', extra_context)
