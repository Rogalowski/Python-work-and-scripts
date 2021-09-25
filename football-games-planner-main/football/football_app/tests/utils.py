import random
from datetime import timedelta

from django.utils import timezone
from faker import Faker

from football_app.models import GAME_LEVELS, GAME_POSITIONS, FOOTBALL_PITCH_SURFACES, FOOTBALL_PITCH_TYPES, \
    FootballPitch, Game, GameReservation, User

fake = Faker()


def fake_user_data():
    """Generate and return fake user data"""

    first_name = fake.first_name()
    last_name = fake.last_name()
    return {
        'first_name': first_name,
        'last_name': last_name,
        'username': f'{first_name.lower()}{last_name.lower()}',
        'email': f'{first_name.lower()}{last_name.lower()}@example.com',
        'year_of_birth': random.randint(1980, 2010),
        'password': 'testowehaslo',
    }


def fake_football_pitch_data():
    """Generate and return fake football pitch data"""

    return {
        'name': fake.company(),
        'type': random.choice(FOOTBALL_PITCH_TYPES)[0],
        'surface': random.choice(FOOTBALL_PITCH_SURFACES)[0],
        'locker_room_available': fake.boolean(chance_of_getting_true=50),
        'city': fake.city(),
        'street': f'{fake.street_name()} {random.randint(1, 100)}',
        'description': fake.text(random.randint(64, 128)),
    }


def fake_game_data():
    """Generate and return fake football pitch data"""

    duration_time = (30, 45, 60, 90)
    number_of_players = (6, 8, 10, 12, 16, 20, 22)

    return {
        'football_pitch': create_fake_football_pitch(),
        'date': timezone.now() + timedelta(hours=2),
        'duration': random.choice(duration_time),
        'level': random.choice(GAME_LEVELS)[0],
        'player_count': random.choice(number_of_players),
        'player_age_from': random.randint(10, 15),
        'player_age_to': random.randint(16, 45),
        'created_by': create_fake_user(),
    }


def fake_future_reservation_data():
    """Generate and return fake future reservation data"""

    return {
        'game': create_fake_future_game(),
        'user': create_fake_user(),
        'preferred_position': random.choice(GAME_POSITIONS)[0],
        'user_has_ball': fake.boolean(chance_of_getting_true=50),
        'is_commented': False,
    }


def fake_past_reservation_data():
    """Generate and return fake past reservation data"""

    return {
        'game': create_fake_past_game(),
        'user': create_fake_user(),
        'preferred_position': random.choice(GAME_POSITIONS)[0],
        'user_has_ball': fake.boolean(chance_of_getting_true=50),
        'is_commented': False,
    }


def create_fake_user():
    """Generate, save to database and return fake user"""

    fake_user = fake_user_data()

    return User.objects.create_user(
        username=fake_user['username'],
        first_name=fake_user['first_name'],
        last_name=fake_user['last_name'],
        email=fake_user['email'],
        year_of_birth=fake_user['year_of_birth'],
        password=fake_user['password'],
    )


def create_fake_football_pitch():
    """Generate, save to database and return fake football pitch"""

    fake_football_pitch = fake_football_pitch_data()

    return FootballPitch.objects.create(
        name=fake_football_pitch['name'],
        type=fake_football_pitch['type'],
        surface=fake_football_pitch['surface'],
        locker_room_available=fake_football_pitch['locker_room_available'],
        city=fake_football_pitch['city'],
        street=fake_football_pitch['street'],
        description=fake_football_pitch['description'],
    )


def create_fake_future_game():
    """Generate, save to database and return fake future football game"""

    fake_game = fake_game_data()

    return Game.objects.create(
        football_pitch=fake_game['football_pitch'],
        date=fake_game['date'],
        duration=fake_game['duration'],
        level=fake_game['level'],
        player_count=fake_game['player_count'],
        player_age_from=fake_game['player_age_from'],
        player_age_to=fake_game['player_age_to'],
        created_by=fake_game['created_by'],
    )


def create_fake_past_game():
    """Generate, save to database and return fake past football game"""

    fake_game = fake_game_data()
    fake_game['date'] = timezone.now() - timedelta(hours=2)

    return Game.objects.create(
        football_pitch=fake_game['football_pitch'],
        date=fake_game['date'],
        duration=fake_game['duration'],
        level=fake_game['level'],
        player_count=fake_game['player_count'],
        player_age_from=fake_game['player_age_from'],
        player_age_to=fake_game['player_age_to'],
        created_by=fake_game['created_by'],
    )


def create_fake_future_reservation():
    """Generate, save to database and return fake future reservation"""

    fake_reservation = fake_future_reservation_data()

    return GameReservation.objects.create(
        game=fake_reservation['game'],
        user=fake_reservation['user'],
        preferred_position=fake_reservation['preferred_position'],
        user_has_ball=fake_reservation['user_has_ball'],
        is_commented=fake_reservation['is_commented'],
    )


def create_fake_past_reservation():
    """Generate, save to database and return fake past reservation"""

    fake_reservation = fake_past_reservation_data()

    return GameReservation.objects.create(
        game=fake_reservation['game'],
        user=fake_reservation['user'],
        preferred_position=fake_reservation['preferred_position'],
        user_has_ball=fake_reservation['user_has_ball'],
        is_commented=fake_reservation['is_commented'],
    )
