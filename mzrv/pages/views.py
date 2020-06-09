from django.shortcuts import render


def index(request):
    extra_context = {
        'page': 'Jogos',
        'games': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Red Dead Redemption 2',
                'price': '199.99',
            }
        ],
        'consoles': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'PlayStation 4 1TB',
                'price': '1899.99',
            }
        ],
        'acessories': [
            {
                'img': 'https://via.placeholder.com/150',
                'title': 'Controle Dualshock 4 - PlayStation 4 - Preto',
                'price': '159.99',
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
            }
        ]
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
