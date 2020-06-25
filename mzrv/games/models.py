from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_photo = models.ImageField(upload_to='photos/games/')
    plataform = ArrayField(models.CharField(max_length=200))
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ('-created_at',)
        verbose_name = 'Jogo'
