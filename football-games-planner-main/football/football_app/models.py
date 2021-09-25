from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone

COMMENT_TYPES = (
    (1, 'Positive'),
    (2, 'Negative'),
)

FOOTBALL_PITCH_SURFACES = (
    (1, "Grass"),
    (2, "Synthetic grass"),
    (3, "Tartan"),
    (4, "Parquet"),
)

FOOTBALL_PITCH_TYPES = (
    (1, "Sports hall"),
    (2, "Orlik pitch"),
    (3, "Stadium"),
)

GAME_LEVELS = (
    (1, "Beginner"),
    (2, "Medium"),
    (3, "Intermediate"),
    (4, "Advanced"),
)

GAME_POSITIONS = (
    (1, "Goalkeeper"),
    (2, "Defender"),
    (3, "Midfielder"),
    (4, "Forward"),
)


class User(AbstractUser):
    """Stores a single user entry."""
    year_of_birth = models.IntegerField(null=True)
    games = models.ManyToManyField('Game', through='GameReservation')


class FootballPitch(models.Model):
    """Stores a single football pitch entry."""
    name = models.CharField(max_length=64)
    type = models.IntegerField(choices=FOOTBALL_PITCH_TYPES)
    surface = models.IntegerField(choices=FOOTBALL_PITCH_SURFACES)
    locker_room_available = models.BooleanField(default=False)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.city} - {self.street}"

    @property
    def rating(self):
        """Return percent of positive `FootballPitch` comments."""
        positive_comments = Comment.objects.filter(football_pitch=self.pk, type=1).count()
        negative_comments = Comment.objects.filter(football_pitch=self.pk, type=2).count()
        try:
            return round((positive_comments / (positive_comments + negative_comments) * 100), 1)
        except ZeroDivisionError:
            return 0


class Comment(models.Model):
    """Stores a single comment entry, related to :model:`football_app.User`
    and :model:`football_app.FootballPitch`
    """
    football_pitch = models.ForeignKey(FootballPitch, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(choices=COMMENT_TYPES, verbose_name="Comment type")
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.football_pitch.name}, {self.user}"

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        return reverse('user_games', kwargs={'pk': self.user.pk})


class GameManager(models.Manager):
    def active_games(self):
        """Return `Games` with a start date at least
        10 minutes earlier than the current time.
        """
        return self.filter(date__gt=timezone.now() + timedelta(minutes=10)).order_by('date')


class Game(models.Model):
    """Stores a single game entry, related to :model:`football_app.User`
    and :model:`football_app.FootballPitch`
    """
    football_pitch = models.ForeignKey(FootballPitch, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.IntegerField()
    level = models.IntegerField(choices=GAME_LEVELS)
    player_count = models.IntegerField()
    player_age_from = models.IntegerField()
    player_age_to = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = GameManager()

    def get_absolute_url(self):
        return reverse('game_details', kwargs={'pk': self.pk})


class GameReservation(models.Model):
    """Stores a single game reservation entry, related to
    :model:`football_app.User` and :model:`football_app.FootballPitch`
    """
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferred_position = models.IntegerField(choices=GAME_POSITIONS)
    user_has_ball = models.BooleanField(default=False, verbose_name="I'll bring the ball")
    is_commented = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('game_details', kwargs={'pk': self.game.pk})
