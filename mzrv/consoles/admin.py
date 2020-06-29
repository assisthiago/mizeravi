from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .filters import PlataformFilter
from .forms import ConsoleForm
from .models import Consoles


class ConsoleAdmin(admin.ModelAdmin):
    form = ConsoleForm

    list_display = (
        'name',
        'price',
        'plataforms',
        'created_at',
    )

    list_filter = (
        PlataformFilter,
        ('created_at', DateRangeFilter),
    )

    ordering = ('name',)


admin.site.register(Consoles, ConsoleAdmin)
