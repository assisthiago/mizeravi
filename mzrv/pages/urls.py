from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acessories', views.acessories, name='acessories'),
    path('consoles', views.consoles, name='consoles'),
    path('games', views.games, name='games'),
]
