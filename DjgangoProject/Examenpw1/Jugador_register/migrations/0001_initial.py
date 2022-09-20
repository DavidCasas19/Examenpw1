# Generated by Django 4.1.1 on 2022-09-19 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stadium', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('points', models.IntegerField(default=0)),
                ('matches_played', models.IntegerField(default=0)),
                ('matches_won', models.IntegerField(default=0)),
                ('matches_drawn', models.IntegerField(default=0)),
                ('matches_lost', models.IntegerField(default=0)),
                ('stadium', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Jugador_register.stadium')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jugador_register.position')),
                ('team', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Jugador_register.team')),
            ],
        ),
    ]
