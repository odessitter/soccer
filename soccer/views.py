from django.shortcuts import render
from soccer.models import Game


def index(request):
    games = Game.objects.all().order_by('home_team__league')
    context = {
        'games': games
    }
    return render(request, 'index.html', context)
