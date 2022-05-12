from django.contrib import admin

from football_app.models import User, FootballPitch, Game, GameReservation, Comment

admin.site.register(User)
admin.site.register(FootballPitch)
admin.site.register(Game)
admin.site.register(GameReservation)
admin.site.register(Comment)
