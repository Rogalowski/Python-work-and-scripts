import random
from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone
from faker import Faker

from football_app.models import FootballPitch, Game, User, GAME_LEVELS

fake = Faker(locale='pl_PL')


class Command(BaseCommand):
    """Generate and save to database 6 to 9 random football games
    for each football pitch existing in database.
    """
    help = "Generate and save to database random football games"

    def handle(self, *args, **kwargs):
        football_pitches = FootballPitch.objects.all()
        users = User.objects.all()
        duration_time = (30, 45, 60, 90)
        number_of_players = (10, 12, 16)

        for football_pitch in football_pitches:
            for _ in range(random.randint(6, 9)):
                dates = (
                    timezone.now() + timedelta(days=random.randint(1, 90), minutes=random.randint(1, 1440)),
                    timezone.now() - timedelta(days=random.randint(1, 90), minutes=random.randint(1, 1440)),
                )
                date = random.choice(dates)
                duration = random.choice(duration_time)
                level = random.choice(GAME_LEVELS)[0]
                player_count = random.choice(number_of_players)
                player_age_from = random.randint(10, 15)
                player_age_to = random.randint(16, 45)
                created_by = random.choice(users)

                Game.objects.create(
                    football_pitch=football_pitch,
                    date=date,
                    duration=duration,
                    level=level,
                    player_count=player_count,
                    player_age_from=player_age_from,
                    player_age_to=player_age_to,
                    created_by=created_by,
                )
