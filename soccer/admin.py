from django.contrib import admin

from soccer.models import Country, League, Game, Team

# Register your models here.
admin.site.register(Country)
admin.site.register(League)
admin.site.register(Game)
admin.site.register(Team)
