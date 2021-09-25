from django.urls import path

from football_app import views as football

urlpatterns = [
    path('', football.HomeView.as_view(), name='home'),
    path('games/', football.GameListView.as_view(), name='games'),
    path('game/<int:pk>/', football.GameDetailView.as_view(), name='game_details'),
    path('add_game/', football.AddGameView.as_view(), name='add_game'),
    path('add_reservation/', football.AddReservationView.as_view(), name='add_reservation'),
    path('my_games/<int:pk>/', football.UserGamesView.as_view(), name='user_games'),
    path('reservation/<int:pk>/comment/', football.AddCommentView.as_view(), name='add_comment'),
    path('game/<int:pk>/remove/', football.DeleteGameView.as_view(), name='delete_game'),
    path('reservation/<int:pk>/remove/', football.DeleteUserReservationView.as_view(), name='delete_reservation'),
    path('football_pitches/', football.FootballPitchListView.as_view(), name='football_pitches'),
    path('football_pitch/<int:pk>/', football.FootballPitchDetailView.as_view(), name='football_pitch_details'),
]
