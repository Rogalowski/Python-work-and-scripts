import random
from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone
from faker import Faker

from football_app.models import Comment, Game, GameReservation, User, COMMENT_TYPES, GAME_POSITIONS

fake = Faker(locale='pl_PL')


class Command(BaseCommand):
    """Generate and save to database random past and future football game
    reservations.

    For random reservations that are past generate user comments and set
    game reservation attribute 'is_commented' to True.
    """
    help = "Add random game reservations to database."

    def handle(self, *args, **kwargs):
        games_count = Game.objects.count()
        games = Game.objects.all().order_by('?')[:int(games_count * 0.8)]

        for game in games:
            users = User.objects.all().order_by('?')[:game.player_count - random.randint(0, 4)]
            for user in users:
                preferred_position = random.choice(GAME_POSITIONS)[0]
                user_has_ball = fake.boolean(chance_of_getting_true=50)

                if game.date < timezone.now():
                    add_comment = fake.boolean(chance_of_getting_true=50)
                    if add_comment:
                        is_commented = True
                        Comment.objects.create(
                            football_pitch=game.football_pitch,
                            user=user,
                            type=random.choice(COMMENT_TYPES)[0],
                            description=fake.text(random.randint(64, 128)),
                            date_added=game.date + timedelta(minutes=(game.duration + random.randint(60, 360))),
                        )
                    else:
                        is_commented = False
                else:
                    is_commented = False

                GameReservation.objects.create(
                    game=game,
                    user=user,
                    preferred_position=preferred_position,
                    user_has_ball=user_has_ball,
                    is_commented=is_commented,
                )
