from django.shortcuts import render

from accessories.forms import PLATAFORM_CHOICES as ACCESSORIES_PLATAFORM_CHOICES
from consoles.forms import PLATAFORM_CHOICES as CONSOLE_PLATAFORM_CHOICES
from games.forms import PLATAFORM_CHOICES as GAME_PLATAFORM_CHOICES

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
    plataform_choices = [plataform[0] for plataform in GAME_PLATAFORM_CHOICES]

    extra_context = {
        'page': 'Jogos',
        'objects': games,
        'filter': {'plataform_choices': plataform_choices}
    }
    return render(request, 'pages/listings.html', extra_context)

def consoles(request):
    consoles = Consoles.objects.all()
    plataform_choices = [plataform[0] for plataform in CONSOLE_PLATAFORM_CHOICES]

    extra_context = {
        'page': 'Videogames',
        'objects': consoles,
        'filter': {'plataform_choices': plataform_choices}
    }
    return render(request, 'pages/listings.html', extra_context)

def accessories(request):
    accessories = Accessories.objects.all()
    plataform_choices = [plataform[0] for plataform in ACCESSORIES_PLATAFORM_CHOICES]

    extra_context = {
        'page': 'Acessórios',
        'objects': accessories,
        'filter': {'plataform_choices': plataform_choices}
    }
    return render(request, 'pages/listings.html', extra_context)
