# Generated by Django 3.0.7 on 2020-06-29 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessories',
            options={'ordering': ('name',), 'verbose_name': 'Accessório'},
        ),
        migrations.RenameField(
            model_name='accessories',
            old_name='plataform',
            new_name='plataforms',
        ),
    ]