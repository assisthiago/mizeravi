from django.contrib.admin import SimpleListFilter

from .forms import PLATAFORMS_CHOICES


class PlataformsFilter(SimpleListFilter):
    title = 'Plataforma'
    parameter_name = 'plataforms'

    def lookups(self, request, model_admin):
        return PLATAFORMS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(plataforms__contains=[self.value()])

        return queryset.all()
