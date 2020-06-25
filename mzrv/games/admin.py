from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .filters import PlataformsFilter
from .forms import GameForm
from .models import Games


class GameAdmin(admin.ModelAdmin):
    form = GameForm

    list_display = (
        'name',
        'price',
        'plataforms',
        'created_at',
    )

    list_filter = (
        PlataformsFilter,
        ('created_at', DateRangeFilter),
    )

    ordering = ('name',)


admin.site.register(Games, GameAdmin)
