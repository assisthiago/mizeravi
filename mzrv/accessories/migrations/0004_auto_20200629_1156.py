# Generated by Django 3.0.7 on 2020-06-29 14:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0003_auto_20200629_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessories',
            name='plataforms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None, verbose_name='Plataformas'),
        ),
    ]