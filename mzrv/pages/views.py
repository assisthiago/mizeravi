from django.shortcuts import render


def index(request):
    extra_context = {
        'page': 'Jogos',
        'games': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Red Dead Redemption 2',
                'price': '199.99',
                'url': '/games/1'
            }
        ],
        'consoles': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Playstation 4',
                'price': '1899.99',
                'url': '/consoles/1'
            }
        ],
        'acessories': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Controle PS4',
                'price': '159.99',
                'url': '/acessories/1'
            }
        ]
    }
    return render(request, 'pages/index.html', extra_context)

def games(request):
    extra_context = {
        'page': 'Jogos',
        'objects': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Red Dead Redemption 2',
                'price': '199.99',
                'url': '/games/1'
            }
        ]
    }
    return render(request, 'pages/listings.html', extra_context)

def consoles(request):
    extra_context = {
        'page': 'Videogames',
        'objects': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Playstation 4',
                'price': '1899.99',
                'url': '/consoles/1'
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
                'title': 'Controle PS4',
                'price': '159.99',
                'url': '/acessories/1'
            }
        ]
    }
    return render(request, 'pages/listings.html', extra_context)
