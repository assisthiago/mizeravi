from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Games(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Nome',)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Preço',)

    main_photo = models.ImageField(
        upload_to='photos/games/',
        verbose_name='Foto',)

    plataforms = ArrayField(
        models.CharField(max_length=200),
        verbose_name='Plataformas')

    created_at = models.DateTimeField(
        default=datetime.now, blank=True,
        verbose_name='Data de criação',)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ('-created_at',)
        verbose_name = 'Jogo'
