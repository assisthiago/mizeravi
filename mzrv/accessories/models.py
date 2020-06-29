from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Accessories(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome')

    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Preço')

    main_photo = models.ImageField(
        upload_to='photos/accessories/',
        verbose_name='Imagem')

    plataforms = ArrayField(
        models.CharField(max_length=200),
        verbose_name='Plataformas')

    created_at = models.DateTimeField(
        default=datetime.now, blank=True,
        verbose_name='Data de Criação')


    def __str__(self):
        return self.name

    class Meta():
        ordering = ('name',)
        verbose_name = 'Acessório'
