import pytest
from django.test import Client

from football_app.tests.utils import create_fake_football_pitch, create_fake_future_game, \
    create_fake_future_reservation, create_fake_past_game, create_fake_past_reservation, create_fake_user


@pytest.fixture
def client():
    """Return 'Client' object"""
    client = Client()
    return client


@pytest.fixture
def fake_user():
    """Return fake `User` object"""
    return create_fake_user()


@pytest.fixture
def fake_football_pitch():
    """Return fake `FootballPitch` object"""
    return create_fake_football_pitch()


@pytest.fixture
def fake_future_game():
    """Return fake future `Game` object"""
    return create_fake_future_game()


@pytest.fixture
def fake_past_game():
    """Return fake past `Game` object"""
    return create_fake_past_game()


@pytest.fixture
def fake_future_reservation():
    """Return fake future `GameReservation` object"""
    return create_fake_future_reservation()


@pytest.fixture
def fake_past_reservation():
    """Return fake past `GameReservation` object"""
    return create_fake_past_reservation()
