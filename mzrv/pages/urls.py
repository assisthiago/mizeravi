from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accessories', views.accessories, name='accessories'),
    path('consoles', views.consoles, name='consoles'),
    path('games', views.games, name='games'),
]
