# Generated by Django 3.0.7 on 2020-06-29 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200625_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ('name',), 'verbose_name': 'Jogo'},
        ),
    ]
