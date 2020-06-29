from django.contrib.admin import SimpleListFilter

from consoles.forms import PLATAFORMS_CHOICES


class PlataformFilter(SimpleListFilter):
    title = 'Plataforma'
    parameter_name = 'plataforms'

    def lookups(self, request, model_admin):
        return PLATAFORMS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(plataforms=self.value())

        return queryset.all()
