from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import (
    Comment, FootballPitch, Game, GameReservation, COMMENT_TYPES, GAME_LEVELS,
    GAME_POSITIONS
)


class AddGameForm(forms.ModelForm):
    """Form for adding the 'Game' object to the database.

    Form validates the correctness of the entered data.
    """
    football_pitch = forms.ModelChoiceField(
        queryset=FootballPitch.objects.all().order_by('name'),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    duration = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration'}),
        min_value=0,
        max_value=720
    )
    player_count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Player count'}),
        min_value=0,
        max_value=50
    )
    player_age_from = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Player age from'}),
        min_value=0,
        max_value=120
    )
    player_age_to = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Player age to'}),
        min_value=0,
        max_value=120
    )

    class Meta:
        model = Game
        fields = (
            'football_pitch', 'date', 'duration', 'level', 'player_count', 'player_age_from', 'player_age_to'
        )

        widgets = {
            'football_pitch': forms.Select(
                attrs={'class': 'form-control'}
            ),
            'level': forms.Select(
                choices=GAME_LEVELS,
                attrs={'class': 'form-control'}
            ),
            'date': forms.DateTimeInput(
                format='%d/%m/%Y %H:%M',
                attrs={'class': 'form-control', 'type': 'datetime-local'}
            )
        }

    def clean(self):
        cleaned_data = super(AddGameForm, self).clean()
        football_pitch = cleaned_data.get('football_pitch')
        date = cleaned_data.get('date')
        duration = cleaned_data.get('duration')
        player_age_from = cleaned_data.get('player_age_from')
        player_age_to = cleaned_data.get('player_age_to')
        game_start = date
        game_end = date + timedelta(minutes=int(duration))
        games = Game.objects.filter(football_pitch=football_pitch)

        if date < timezone.now():
            self.add_error('date', 'The date cannot be past.')

        if player_age_from > player_age_to:
            self.add_error('player_age_from', "'Player age from' cannot be greater than 'Player age to'.")

        game_time_error = ("It is not possible to add a game. During this time, "
                           f"the football pitch '{football_pitch.name}' is occupied.")

        for game in games:
            game_start_db = game.date
            game_end_db = game.date + timedelta(minutes=game.duration)
            if game_start < game_start_db < game_end:
                self.add_error('date', game_time_error)

            if game_start > game_start_db and game_end < game_end_db:
                self.add_error('date', game_time_error)

            if game_start < game_end_db < game_end:
                self.add_error('date', game_time_error)


class AddReservationForm(forms.ModelForm):
    """Form for adding the 'GameReservation' object to the database."""

    class Meta:
        model = GameReservation
        fields = ('preferred_position', 'user_has_ball', 'game', 'user')

        widgets = {
            'game': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'preferred_position': forms.Select(
                choices=GAME_POSITIONS,
                attrs={'class': 'form-control'}
            ),
            'user_has_ball': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            )
        }


class AddCommentForm(forms.ModelForm):
    """Form for adding the 'Comment' object to the database."""

    class Meta:
        model = Comment
        fields = ('type', 'description')

        widgets = {
            'type': forms.Select(
                choices=COMMENT_TYPES,
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }


class SearchGameForm(forms.ModelForm):
    """`Game` filtering form."""
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Football pitch name'}),
        label='Football pitch name',
        required=False
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
        required=False
    )
    level = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=(
            (0, "---------"),
            (1, "Początkujący"),
            (2, "Średni"),
            (3, "Średnio zaawansowany"),
            (4, "Zaawansowany"),
        ),
        required=False
    )
    date_from = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'},
            format='%d/%m/%Y %H:%M'
        ),
        required=False
    )
    date_to = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'class': 'form-control', 'type': 'datetime-local'},
            format='%d/%m/%Y %H:%M'
        ),
        required=False
    )

    class Meta:
        model = Game
        fields = ('name', 'city', 'level', 'date_from', 'date_to')
