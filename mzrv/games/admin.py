from django.contrib import admin

from .forms import GameForm
from .models import Games


class GameAdmin(admin.ModelAdmin):
    form = GameForm


admin.site.register(Games, GameAdmin)
