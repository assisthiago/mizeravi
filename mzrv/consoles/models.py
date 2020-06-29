from datetime import datetime
from django.db import models


class Consoles(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome')

    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Preço')

    main_photo = models.ImageField(
        upload_to='photos/consoles/',
        verbose_name='Imagem')

    plataforms = models.CharField(
        max_length=200,
        verbose_name='Plataforma')

    created_at = models.DateTimeField(
        default=datetime.now, blank=True,
        verbose_name='Data de Criação')


    def __str__(self):
        return self.name

    class Meta():
        ordering = ('name',)
        verbose_name = 'Videogame'
