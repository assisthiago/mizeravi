from django.contrib import admin

from .models import Consoles


class ConsoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Consoles, ConsoleAdmin)
