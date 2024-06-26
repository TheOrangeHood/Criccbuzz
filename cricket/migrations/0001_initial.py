# Generated by Django 5.0.4 on 2024-04-07 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('batsman', 'Batsman'), ('bowler', 'Bowler'), ('allrounder', 'All Rounder'), ('wicket_keeper', 'Wicket Keeper')], default='batsman', max_length=200)),
                ('matches_played', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('average', models.FloatField(default=0.0)),
                ('strike_rate', models.FloatField(default=0.0)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='cricket.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('upcoming', 'Upcoming'), ('completed', 'Completed')], default='upcoming', max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='cricket.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='cricket.team')),
            ],
        ),
    ]
