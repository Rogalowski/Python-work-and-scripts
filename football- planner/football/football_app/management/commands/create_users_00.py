import random

from django.core.management import BaseCommand
from faker import Faker

from football_app.models import User

fake = Faker()


class Command(BaseCommand):
    """Generate and save to database 60 random users
    with default password: 'testowehaslo'.
    """
    help = "Generate and save to database 60 random users with default password: 'testowehaslo'."

    def handle(self, *args, **kwargs):
        for _ in range(60):
            first_name = fake.first_name()
            last_name = fake.last_name()
            username = f'{first_name.lower()[0]}{last_name.lower()}{random.randint(1, 9)}'
            email = f'{first_name.lower()}{last_name.lower()}@example.com'
            year_of_birth = random.randint(1980, 2010)
            password = 'testowehaslo'

            User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                year_of_birth=year_of_birth,
                password=password,
            )
