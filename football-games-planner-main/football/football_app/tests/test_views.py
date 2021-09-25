from datetime import timedelta

import pytest
from django.utils import timezone

from football_app.models import Comment, Game, GameReservation


@pytest.mark.django_db
def test_add_game_with_future_date(client, fake_user, fake_football_pitch):
    """Test of adding `Game` object with a future game `date`
    to the database.
    """
    games_count = Game.objects.count()
    game = {
        'football_pitch': fake_football_pitch.pk,
        'date': timezone.now() + timedelta(hours=2),
        'duration': 60,
        'level': 2,
        'player_count': 12,
        'player_age_from': 15,
        'player_age_to': 30,
        'created_by': fake_user.pk,
    }
    client.force_login(fake_user)

    response = client.post('/add_game/', game)

    assert response.status_code == 302
    assert Game.objects.count() == games_count + 1
    assert Game.objects.get(football_pitch__name=fake_football_pitch.name)


@pytest.mark.django_db
def test_add_game_with_past_date(client, fake_user, fake_football_pitch):
    """Test of adding `Game` object with a past game `date`
    to the database.
    """
    games_count = Game.objects.count()
    game = {
        'football_pitch': fake_football_pitch.pk,
        'date': timezone.now() - timedelta(hours=2),
        'duration': 60,
        'level': 2,
        'player_count': 12,
        'player_age_from': 15,
        'player_age_to': 30,
        'created_by': fake_user.pk,
    }
    client.force_login(fake_user)

    response = client.post('/add_game/', game)

    assert response.status_code == 200
    assert Game.objects.count() == games_count


@pytest.mark.django_db
def test_add_reservation_for_future_game(client, fake_user, fake_future_game):
    """Test of adding `GameReservation` object for a game with
    a future game `date` to the database.
    """
    reservation_count = GameReservation.objects.count()
    reservation = {
        'game': fake_future_game.pk,
        'user': fake_user.pk,
        'preferred_position': 3,
        'user_has_ball': True,
        'is_commented': False,
    }
    client.force_login(fake_user)

    response = client.post('/add_reservation/', reservation)

    assert response.status_code == 302
    assert GameReservation.objects.count() == reservation_count + 1
    assert GameReservation.objects.get(
        user=fake_user,
        game=fake_future_game,
    )


@pytest.mark.django_db
def test_add_comment(client, fake_past_reservation):
    """Test of adding `Comment` object for the football pitch
    to the database.
    """
    comments_count = Comment.objects.count()
    comment = {
        'football_pitch': fake_past_reservation.game.football_pitch.pk,
        'user': fake_past_reservation.user.pk,
        'type': 1,
        'description': 'Fake comment description'
    }
    client.force_login(fake_past_reservation.user)

    response = client.post(f'/reservation/{fake_past_reservation.pk}/comment/', comment)

    assert response.status_code == 302
    assert Comment.objects.count() == comments_count + 1
    assert Comment.objects.get(
        football_pitch=fake_past_reservation.game.football_pitch,
        user=fake_past_reservation.user,
    )


@pytest.mark.django_db
def test_delete_game(client, fake_user, fake_future_game):
    """Test of removing `Game` object from the database."""
    game_count = Game.objects.count()
    client.force_login(fake_user)

    response = client.delete(f'/game/{fake_future_game.pk}/remove/')

    assert Game.objects.count() == game_count - 1
    assert response.status_code == 302
    game_ids = [game.id for game in Game.objects.all()]
    assert fake_future_game.id not in game_ids
