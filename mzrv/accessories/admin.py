from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .filters import PlataformFilter
from .forms import AccessoryForm
from .models import Accessories


class AccessoryAdmin(admin.ModelAdmin):
    form = AccessoryForm

    list_display = (
        'name',
        'price',
        'plataform',
        'created_at',
    )

    list_filter = (
        PlataformFilter,
        ('created_at', DateRangeFilter),
    )

    ordering = ('name',)


admin.site.register(Accessories, AccessoryAdmin)
