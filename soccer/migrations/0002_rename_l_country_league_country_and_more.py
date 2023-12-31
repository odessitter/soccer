# Generated by Django 4.2.7 on 2023-11-18 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='l_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='league',
            old_name='league',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='league',
            name='client',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccer.league')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('home_team_goals', models.IntegerField(default=0)),
                ('away_team_goals', models.IntegerField(default=0)),
                ('home_team_points', models.IntegerField(default=0)),
                ('away_team_points', models.IntegerField(default=0)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='soccer.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='soccer.team')),
            ],
        ),
    ]
