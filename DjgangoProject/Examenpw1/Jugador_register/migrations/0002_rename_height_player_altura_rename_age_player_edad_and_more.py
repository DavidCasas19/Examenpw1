# Generated by Django 4.1.1 on 2022-09-20 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jugador_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='height',
            new_name='Altura',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='age',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='weight',
            new_name='peso',
        ),
    ]
