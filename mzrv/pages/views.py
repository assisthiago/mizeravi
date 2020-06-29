from django.shortcuts import render

from accessories.forms import PLATAFORM_CHOICES as ACCESSORIES_PLATAFORM_CHOICES
from consoles.forms import PLATAFORM_CHOICES as CONSOLE_PLATAFORM_CHOICES
from games.forms import PLATAFORM_CHOICES as GAME_PLATAFORM_CHOICES

from accessories.models import Accessories
from consoles.models import Consoles
from games.models import Games

from . import helpers

def index(request):
    if bool(request.GET):
        search_lookups = helpers.build_search_lookups(request)

        accessories = Accessories.objects.filter(
            search_lookups).order_by('-created_at')
        consoles = Consoles.objects.filter(
            search_lookups).order_by('-created_at')
        games = Games.objects.filter(
            search_lookups).order_by('-created_at')
    else:
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
    if bool(request.GET):
        plataform_lookup, price_lookup = helpers.build_filters_lookups(request, 'games')
        games = Games.objects.filter(plataform_lookup, price_lookup)
    else:
        games = Games.objects.all()

    plataform_filter, price_filter = helpers.check_which_filter_is_selected(request)
    plataform_choices = [plataform[0] for plataform in GAME_PLATAFORM_CHOICES]

    extra_context = {
        'page': 'Jogos',
        'objects': games,
        'filter': {
            'plataform_choices': plataform_choices,
            'filters_selected': {
                'plataform': plataform_filter,
                'price': price_filter
            }
        }
    }
    return render(request, 'pages/listings.html', extra_context)

def consoles(request):
    if bool(request.GET):
        plataform_lookup, price_lookup = helpers.build_filters_lookups(request, 'consoles')
        consoles = Consoles.objects.filter(plataform_lookup, price_lookup)
    else:
        consoles = Consoles.objects.all()

    plataform_filter, price_filter = helpers.check_which_filter_is_selected(request)
    plataform_choices = [plataform[0] for plataform in CONSOLE_PLATAFORM_CHOICES]

    extra_context = {
        'page': 'Videogames',
        'objects': consoles,
        'filter': {
            'plataform_choices': plataform_choices,
            'filters_selected': {
                'plataform': plataform_filter,
                'price': price_filter
            }
        }
    }
    return render(request, 'pages/listings.html', extra_context)

def accessories(request):
    if bool(request.GET):
        plataform_lookup, price_lookup = helpers.build_filters_lookups(request, 'accessories')
        accessories = Accessories.objects.filter(plataform_lookup, price_lookup)
    else:
        accessories = Accessories.objects.all()

    plataform_filter, price_filter = helpers.check_which_filter_is_selected(request)
    plataform_choices = [plataform[0] for plataform in ACCESSORIES_PLATAFORM_CHOICES]

    extra_context = {
        'page': 'Acessórios',
        'objects': accessories,
        'filter': {
            'plataform_choices': plataform_choices,
            'filters_selected': {
                'plataform': plataform_filter,
                'price': price_filter
            }
        }
    }
    return render(request, 'pages/listings.html', extra_context)
