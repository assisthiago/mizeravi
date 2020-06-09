from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games', views.games, name='games'),
    path('consoles', views.consoles, name='consoles'),
    path('acessories', views.acessories, name='acessories'),
]
