import random

from django.core.management import BaseCommand
from faker import Faker

from football_app.models import FootballPitch, FOOTBALL_PITCH_SURFACES, FOOTBALL_PITCH_TYPES

fake = Faker()


class Command(BaseCommand):
    """Generate and save to database 35 random football pitches."""
    help = "Generate and save to database 35 random football pitches."

    def handle(self, *args, **kwargs):
        for _ in range(35):
            name = fake.company()
            type = random.choice(FOOTBALL_PITCH_TYPES)[0]
            surface = random.choice(FOOTBALL_PITCH_SURFACES)[0]
            locker_room_available = fake.boolean(chance_of_getting_true=50)
            city = fake.city()
            street = f'{fake.street_name()} {random.randint(1, 100)}'
            description = fake.text(random.randint(64, 128))

            FootballPitch.objects.create(
                name=name,
                type=type,
                surface=surface,
                locker_room_available=locker_room_available,
                city=city,
                street=street,
                description=description,
            )
