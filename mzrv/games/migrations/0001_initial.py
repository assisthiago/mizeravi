# Generated by Django 3.0.7 on 2020-06-25 22:03

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('main_photo', models.ImageField(upload_to='photos/games/', verbose_name='Foto')),
                ('plataforms', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None, verbose_name='Plataformas')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Jogo',
                'ordering': ('-created_at',),
            },
        ),
    ]
