# Football Games Planner App 

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jaksli474/football-games-planner.git
$ cd football-games-planner
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a created virtual
environment.

Once `pip` has finished downloading the dependencies:

```sh
(env)$ cd football/football
(env)$ touch local_settings.py
```

And create database connection according to the django documentation.

https://docs.djangoproject.com/en/3.2/ref/settings/#databases <br/>
https://docs.djangoproject.com/en/3.2/ref/databases/

Next step is to make migrations and run app:

```sh
(env)$ cd ../
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

## Load database with sample data

Database can be updated with sample fake data:

- Users
- Football pitches
- Games
- Reservations
- Comments

Fake data commands description:

- create_users_00 - command generate 60 random users with password 'testowehaslo'.


- create_football_pitches_01 - command generate 35 random football pitches.


- create_games_02 - command generate 6 to 9 random football games for each football pitch existing in database.


- create_game_reservations_03 - command generate random past and future football game reservations.

  For random reservations that are past generate user comments and set game reservation attribute 'is_commented' to
  True. <br/><br/>

To load the database with sample fake data follow steps:

```sh
(env)$ python manage.py create_users_00
(env)$ python manage.py create_football_pitches_01
(env)$ python manage.py create_games_02
(env)$ python manage.py create_game_reservations_03
```

## Tests

To run the tests, `cd` into the directory `../football-games-planner/football/football_app/tests/` and run:

```sh
(env)$ pytest test_views.py
```

## App Description

Football Games Planner App

The application is used to manage football games. Allows logged in users to add announcements about future 
football games. Users can take part in games by making reservations.

The application allows:

- Not logged in user:
  - browse available football games


- Logged in user:
  - browse for available football games
  - view game details
  - add games
  - delete user games
  - make a reservation for a game
  - delete user reservation
  - view football pitch comments
  - add comments to the football pitches
  - browse for football pitches
  - view football pitch details
  - view the user's page with games related to the user
