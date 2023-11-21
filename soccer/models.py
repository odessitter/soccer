from django.db import models


# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=50)
    img = models.ImageField(upload_to='Country', null=True, blank=True)

    def __str__(self):
        return self.country


class League(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=150)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Game(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    date = models.DateField(auto_now=True)
    home_team_goals = models.IntegerField(default=0)
    away_team_goals = models.IntegerField(default=0)
    home_team_points = models.IntegerField(default=0)
    away_team_points = models.IntegerField(default=0)

    def __str__(self):
        return self.home_team.name + ' - ' + self.away_team.name
