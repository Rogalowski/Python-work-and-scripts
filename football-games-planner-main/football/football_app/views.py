from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from football_app.forms import AddCommentForm, AddGameForm, AddReservationForm, SearchGameForm
from football_app.models import Comment, FootballPitch, Game, GameReservation, User


class BaseGameView(ListView):
    """Returns sorted and filtered games."""

    def get_queryset(self):
        """Retrieves form data and returns queryset
        with filtered and sorted `Game` data.
        """
        queryset = Game.objects.active_games()

        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        level = self.request.GET.get('level')
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        sort_by = self.request.GET.get('sort_by')

        # sorting
        if sort_by == 'football_pitch_desc':
            queryset = queryset.order_by('football_pitch__name', 'date')

        if sort_by == 'football_pitch_asc':
            queryset = queryset.order_by('-football_pitch__name', 'date')

        if sort_by == 'date_desc':
            queryset = queryset.order_by('date')

        if sort_by == 'date_asc':
            queryset = queryset.order_by('-date')

        # filtering
        if name:
            football_pitch = FootballPitch.objects.filter(name__icontains=name)
            queryset = queryset.filter(football_pitch__in=football_pitch)

        if city:
            football_pitch = FootballPitch.objects.filter(city__icontains=city)
            queryset = queryset.filter(football_pitch__in=football_pitch)

        if level:
            if level != '0':
                queryset = queryset.filter(level=level)

        if date_from:
            queryset = queryset.filter(date__gte=date_from)

        if date_to:
            queryset = queryset.filter(date__lte=date_to)

        return queryset

    def get_context_data(self, **kwargs):
        """Returns an extra context data.

        **Context**

        ``form``
            Form data with initial values of current filtering.

        ``sort_by``
            Current sort type.
        """
        context = super(BaseGameView, self).get_context_data(**kwargs)
        context['form'] = SearchGameForm(
            initial={
                'name': self.request.GET.get('name'),
                'city': self.request.GET.get('city'),
                'level': self.request.GET.get('level'),
                'date_from': self.request.GET.get('date_from'),
                'date_to': self.request.GET.get('date_to'),
            }
        )
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


class HomeView(BaseGameView):
    """Returns 5 upcoming games and 3
    football pitches with the best rating.
    """
    model = Game
    template_name = 'football_app/home.html'

    def get_queryset(self):
        """Returns queryset with 5 upcoming `Game` objects."""
        return super().get_queryset()[:5]

    def get_context_data(self, **kwargs):
        """Returns an extra context data.

        **Context**

            ``best_football_pitches``
                3 instances of :model: `football_app.FootballPitch`
                with the best rating in the database.
        """
        context = super(HomeView, self).get_context_data(**kwargs)
        best_football_pitches = sorted(FootballPitch.objects.all(), key=lambda f: f.rating, reverse=True)
        best_football_pitches = best_football_pitches[:3]
        context['best_football_pitches'] = best_football_pitches
        return context


class GameListView(BaseGameView):
    """Returns filtered and sorted future `Game` objects.

    Pagination by 12 games.
    """
    model = Game
    template_name = 'football_app/games.html'
    paginate_by = 12


class GameDetailView(LoginRequiredMixin, DetailView):
    """Returns individual `Game` object and an extra
    context data.
    """
    model = Game
    template_name = 'football_app/game_details.html'

    def get_context_data(self, **kwargs):
        """Returns an extra context.

        **Context**

            ``user_age``
                Current logged in `User` age.

            ``existing_user_reservation``
                Current logged in `User` reservation for `Game` object.

            ``positive_comments``
                `FootballPitch` object positive comments.

            ``negative_comments``
                `FootballPitch` object negative comments.

            ``reservations_count``
                Reservations count for `Game` object.

            ``available_positions``
                Available positions count for `Game` object.

            ``future_game``
                Information if `Game` object date is past or future.

            ``past_reservations``
                Past `GameReservation` objects related to `Game` object.
        """
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context['form'] = AddReservationForm(initial={'game': context['game'].id, 'user': self.request.user.id})
        game = Game.objects.get(pk=context['game'].id)
        reservations_count = GameReservation.objects.filter(game=context['game'].id).count()
        existing_user_reservation = GameReservation.objects.filter(game=game, user=self.request.user)
        past_reservations = GameReservation.objects.filter(game__in=Game.objects.filter(date__lt=timezone.now()))
        year_of_birth = User.objects.get(pk=self.request.user.id).year_of_birth

        if game.date > timezone.now():
            future_game = True
        else:
            future_game = False

        if year_of_birth:
            user_age = timezone.now().year - year_of_birth
        else:
            user_age = 15

        context['user_age'] = user_age
        context['existing_user_reservation'] = existing_user_reservation
        context['positive_comments'] = game.football_pitch.comments.filter(type=1)
        context['negative_comments'] = game.football_pitch.comments.filter(type=2)
        context['reservations_count'] = reservations_count
        context['available_positions'] = game.player_count - reservations_count
        context['future_game'] = future_game
        context['past_reservations'] = past_reservations
        return context


class AddReservationView(CreateView):
    """Returns form for adding a new game reservation."""
    model = GameReservation
    form_class = AddReservationForm


class AddCommentView(LoginRequiredMixin, CreateView):
    """Returns form for adding a new comment for football pitch."""
    model = Comment
    form_class = AddCommentForm
    template_name = 'football_app/add_comment.html'

    def get_context_data(self, **kwargs):
        """Returns an extra context data.

        **Context**

            ``reservation``
                An instance of :model: `football_app.GameReservation`
        """
        context = super(AddCommentView, self).get_context_data(**kwargs)
        context['reservation'] = GameReservation.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """Sets the currently logged in user as the
        author of the comment.

        Assigns a comment to the football pitch from the reservation.
        """
        reservation = GameReservation.objects.get(pk=self.kwargs['pk'])
        form.instance.football_pitch_id = reservation.game.football_pitch.id
        form.instance.user = self.request.user
        reservation.is_commented = True
        reservation.save()
        return super().form_valid(form)


class AddGameView(LoginRequiredMixin, CreateView):
    """Returns form for adding a new game"""
    model = Game
    form_class = AddGameForm
    template_name = 'football_app/add_game.html'

    def form_valid(self, form):
        """Sets the currently logged in user as the
        creator of the game.
        """
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UserGamesView(LoginRequiredMixin, ListView):
    """Returns `GameReservation` objects and an extra
     context.
    """
    model = GameReservation
    template_name = 'football_app/user_games.html'

    def get_context_data(self, **kwargs):
        """Returns an extra context data.

        **Context**

            ``organized_games``
                Future games organized by the currently logged in user.

            ``upcoming_games``
                Future games for which the currently logged in user
                has reservation.

            ``past_games``
                Past games for which the currently logged in user
                had reservation.

            ``reservations_count``
                Total number of reservations for the next game
                of the currently logged in user.
        """
        context = super(UserGamesView, self).get_context_data(**kwargs)
        organized_games = Game.objects.filter(created_by=self.request.user, date__gt=timezone.now()).order_by('date')
        upcoming_games = self.request.user.games.filter(date__gt=timezone.now()).order_by('date')
        past_games = self.request.user.games.filter(date__lte=timezone.now()).order_by('-date')
        try:
            reservations_count = GameReservation.objects.filter(game=upcoming_games.first().id).count()
        except AttributeError:
            reservations_count = 0
        context['organized_games'] = organized_games
        context['upcoming_games'] = upcoming_games
        context['past_games'] = past_games
        context['reservations_count'] = reservations_count
        return context


class DeleteGameView(LoginRequiredMixin, DeleteView):
    """Returns form for removing a `Game` object from database"""
    model = Game
    template_name = 'football_app/delete_game.html'

    def get_queryset(self):
        """Returns future `Game` objects created by current logged
        in user.
        """
        context = Game.objects.filter(date__gte=timezone.now())
        return context

    def get_success_url(self):
        """After deleting `Game` object redirects the user
        to the 'user_games' template.
        """
        return reverse_lazy('user_games', kwargs={'pk': self.request.user.id})


class DeleteUserReservationView(LoginRequiredMixin, DeleteView):
    """Returns form for removing a game reservation"""
    model = GameReservation
    template_name = 'football_app/delete_reservation.html'

    def get_queryset(self):
        """Returns future `GameReservation` objects created by current logged
        in user.
        """
        games = Game.objects.filter(date__gte=timezone.now())
        queryset = GameReservation.objects.filter(game__in=games, user=self.request.user.id)
        return queryset

    def get_success_url(self):
        """After deleting `GameReservation` object redirects the user
        to the 'game_details' template.
        """
        game_id = self.request.POST.get('game_id')
        return reverse_lazy('game_details', kwargs={'pk': game_id})


class FootballPitchListView(LoginRequiredMixin, ListView):
    """Returns `FootballPitch` objects ordered descending
    by rating.

    Pagination by 5 football pitches.
    """
    model = FootballPitch
    template_name = 'football_app/football_pitches.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        """Returns an extra context data.

            **Context**

                ``best_football_pitches``
                    3 instances of :model: `football_app.FootballPitch`
                    with the best rating in the database.
        """
        context = super(FootballPitchListView, self).get_context_data(**kwargs)
        best_football_pitches = sorted(FootballPitch.objects.all(), key=lambda f: f.rating, reverse=True)
        best_football_pitches = best_football_pitches[:3]
        context['best_football_pitches'] = best_football_pitches
        return context

    def get_queryset(self):
        """Returns `FootballPitch` objects ordered descending
        by rating.
        """
        queryset = sorted(FootballPitch.objects.all(), key=lambda f: f.rating, reverse=True)
        return queryset


class FootballPitchDetailView(LoginRequiredMixin, DetailView):
    """Returns individual `Game` object and an extra
    context data.
    """
    model = FootballPitch
    context_object_name = 'football_pitch'
    template_name = 'football_app/football_pitch_details.html'

    def get_context_data(self, **kwargs):
        """Returns an extra context.

        **Context**

            ``positive_comments``
                `FootballPitch` object positive comments.

            ``negative_comments``
                `FootballPitch` object negative comments.

            ``upcoming_games``
                Future games to be played on `FootballPitch` object.

            ``past_games``
                Past games played on `FootballPitch` object.
        """
        context = super(FootballPitchDetailView, self).get_context_data(**kwargs)
        pitch = FootballPitch.objects.get(pk=self.kwargs['pk'])
        football_pitch_games = Game.objects.filter(football_pitch=self.kwargs['pk'])
        upcoming_games = football_pitch_games.filter(date__gt=timezone.now()).order_by('date')
        past_games = football_pitch_games.filter(date__lte=timezone.now()).order_by('-date')

        context['upcoming_games'] = upcoming_games
        context['past_games'] = past_games
        context['positive_comments'] = pitch.comments.filter(type=1)
        context['negative_comments'] = pitch.comments.filter(type=2)
        return context
