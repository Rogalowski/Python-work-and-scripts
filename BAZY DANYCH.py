## Zadanie 1 &ndash; zadania rozwiązywane z wykładowcą

Połącz tabele `Products` i `Orders` relacją wiele do wielu. 
Napisz kilka zapytań, które połączą produkty z zamówieniami.

Zapytania umieść w pliku **zadanie1.py**.



create_products_orders = """
CREATE TABLE products_orders (
    product_id INT,
    order_id INT,

    -- złożony klucz podstawowy - para kolumn zamiast jednej
    PRIMARY KEY (product_id, order_id),

    FOREIGN KEY (product_id) REFERENCES products (id),
    FOREIGN KEY (order_id) REFERENCES orders (id)
);
"""

wybieramy = """
SELECT * FROM products
INNER JOIN products_orders ON products.id=products_orders.product_id
INNER JOIN orders ON orders.id=products_orders.order_id;
"""
#  id | name | description | price | product_id | order_id | id | description
# ----+------+-------------+-------+------------+----------+----+-------------
# (0 rows)

jeszcze_raz_wybieramy = """
-- wszystkie produkty, również te niezamówione
SELECT * FROM products
LEFT JOIN products_orders ON products.id=products_orders.product_id
LEFT JOIN orders ON orders.id=products_orders.order_id;
"""
#  id |   name    |         description          | price  | product_id | order_id | id | description
# ----+-----------+------------------------------+--------+------------+----------+----+-------------
#   2 | Książka   | Przygody pewnego programisty |  29.99 |            |          |    |
#   1 | Telewizor | HiperHD                      | 999.99 |            |          |    |
#   3 | Antena    | Specjalny odbiornik          | 200.00 |            |          |    |
# (3 rows)

add_product_order_1 = """
INSERT INTO products_orders (product_id, order_id)
VALUES (1, 2), (2, 2), (3, 1), (3, 3);
"""

wybieramy_ponownie = """
SELECT * FROM products INNER JOIN products_orders ON products.id=products_orders.product_id
INNER JOIN orders ON orders.id=products_orders.order_id;
"""
#  id |   name    |         description          | price  | product_id | order_id | id |        description
# ----+-----------+------------------------------+--------+------------+----------+----+----------------------------
#   1 | Telewizor | HiperHD                      | 999.99 |          1 |        2 |  2 | Polecam tego allegrowicza
#   2 | Książka   | Przygody pewnego programisty |  29.99 |          2 |        2 |  2 | Polecam tego allegrowicza
#   3 | Antena    | Specjalny odbiornik          | 200.00 |          3 |        1 |  1 | Świetny produkt
#   3 | Antena    | Specjalny odbiornik          | 200.00 |          3 |        3 |  3 | Więcej tu nie będę kupować
# (4 rows)





## Zadanie 2 &ndash;

Połącz tabele `Cinemas` i `Movies` poprzez relację wiele do wielu (film może być
wyświetlany w wielu kinach, kino może mieć wiele filmów).

Dodatkowo stworzoną tabelę nazwij `Screening`. Oprócz pól odwołujących się do tabel `Cinemas` i `Movies` powinna mieć 
polę **datetime** typu `timestamp`.

Dodaj kilka seansów.

Zapytania umieść w pliku **zadanie2.py**.


create_screenings_table = """
CREATE TABLE screening
(
id SERIAL NOT NULL,
cinema_id INT,
movie_id INT,
datetime TIMESTAMP,
PRIMARY KEY(id),
PRIMARY KEY(cinema_id, movie_id),
FOREIGN KEY(cinema_id) REFERENCES cinemas(id),
FOREIGN KEY(movie_id) REFERENCES movies(id)  
);
"""
add_screenieng_1 = """
INSERT INTO screening (cinema_id, movie_id, datetime) VALUES
(1, 1, '2019-05-03 12:30:00'),
(2, 1, '2019-05-03'),
(2, 2, '2019-02-02'),
(1, 2, '2020-01-01');
"""

zapytanie = """
SELECT movies.id, movies.name, cinemas.name, screening.datetime FROM movies
JOIN screening ON movies.id=screening.movie_id
JOIN cinemas ON cinemas.id=screening.cinema_id;
"""















CREATE DATABASE cinemas_db;


CREATE TABLE cinemas
(
id serial PRIMARY KEY,
name varchar(100),
address varchar(100)
);

CREATE TABLE movies
(
id serial PRIMARY KEY,
name varchar(100),
description text,
rating smallint
);

CREATE TABLE tickets
(
id serial,
quantity int,
price decimal(5,2),
PRIMARY KEY(id)
);

CREATE TABLE payments
(
id serial,
type char(1), -- G gotowka, K kartka
date date,
PRIMARY KEY(id)
);



CREATE TABLE comments
(
id SERIAL,
content TEXT,
movie_id INT,
PRIMARY KEY(id),
FOREIGN KEY(movie_id) REFERENCES movies(id)
);


INSERT INTO movies(name, description, rating) VALUES ('Harry Potter', 'Film magiczny', 5);
INSERT INTO movies(name, description, rating) VALUES ('Star Wars', 'Film kosmiczny', 4);
INSERT INTO movies(name, description, rating) VALUES ('Wladcy Much', 'Film polski', 3);
INSERT INTO movies(name, description, rating) VALUES ('Kac Vegas', 'Film komediowy', 5);

INSERT INTO tickets(quantity, price) VALUES (3,10.0);
INSERT INTO tickets(quantity, price) VALUES (1,5.5);
INSERT INTO tickets(quantity, price) VALUES (2,20.0);
INSERT INTO tickets(quantity, price) VALUES (2,7.1);

INSERT INTO cinemas (name, address) VALUES
('Helios', 'al. Politechniki, Łódź'),
('Cinema City', 'Manufaktura, Łódź'),
('Multikino - Silver Screen', 'al. Piłsudskiego, Łódź');

INSERT INTO payments (type, date) VALUES  --G gotowka, K karta
('G', '2019-05-03'),
('K', '2019-12-06'),
('K', '2019-07-12'),
('G', '2019-09-02'),
('K', '2019-07-11');


#RELACJA JEDEN DO WIELU

CREATE TABLE comments
(
id SERIAL,
content TEXT,
movie_id INT,
PRIMARY KEY(id),
FOREIGN KEY(movie_id) REFERENCES movies(id)
);


INSERT INTO comments(content, movie_id) VALUES (' Extra', 1);
INSERT INTO comments(content, movie_id) VALUES ('Super', 1);
INSERT INTO comments(content, movie_id) VALUES ('Niee polubilem ', 2);
INSERT INTO comments(content, movie_id) VALUES ('Zajefajny', 3);


# JEDEN DO JEDEN RELACJA
DROP TABLE payments ;

CREATE TABLE payments
(
id SERIAL,
ticket_id INT UNIQUE,
type CHAR(1), -- G gotowka, K kartka
date DATE,
PRIMARY KEY(id),
FOREIGN KEY(ticket_id) REFERENCES tickets(id) ON DELETE CASCADE
);

INSERT INTO payments (ticket_id, type, date) VALUES  --G gotowka, K karta
(1, 'G', '2019-05-03'),
(2, 'K', '2019-12-06'),
(3, 'K', '2019-07-12'),
(4, 'G', '2019-09-02');



# WIELE DO WIELU RELACJA

CREATE TABLE screening
(
id SERIAL NOT NULL,
cinema_id INT,
movie_id INT,
datetime TIMESTAMP,
PRIMARY KEY(cinema_id, movie_id),
FOREIGN KEY(cinema_id) REFERENCES cinemas(id),
FOREIGN KEY(movie_id) REFERENCES movies(id)
);

INSERT INTO screening (cinema_id, movie_id, datetime) VALUES
(1, 1, '2019-05-03'),
(2, 1, '2019-05-03'),
(2, 2, '2019-02-02'),
(1, 2, '2020-01-01');

zapytanie = """
SELECT movies.id, movies.name, cinemas.name, screening.datetime FROM movies
JOIN screening ON movies.id=screening.movie_id
JOIN cinemas ON cinemas.id=screening.cinema_id;
"""













#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO
#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO#BAZY DANYCH DJANGO
#Pełna lista filtrów:
#https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-specific-objects-with-filters



# #ZAPYTANIA NA SHELL# DZIEN 2 ZADANIA MANAGER OBJECT, MODYFIKOWANIE, WYSWIETLANIE, USUWANIE, SORTOWANIE
# ZADANIE 1
# W aplikacji exercises_app, w modelu Band znajduje się kilkanaście zespołów.
#
#     Wyciągnij dane wszystkich zespołów.
#     Posortuj je alfabetycznie.
#     Dodaj dane zespołu Rage Against The Machine, rok założenia 1991.
#
# Zadania roziąż w konsoli interaktywnej (python manage.py shell)
#
# Hint: Jak doinstalujesz ipython (pip install ipython) shell będzie kolorował składnię, oraz podpowiadał komendy przy użyciu przycisku tab
# from exercises_app.models import Band
#

# In [4]: # Wyciągnij dane wszystkich zespołów.
# In [5]: Band.objects.all()
# Out[5]: <QuerySet [<Band: Band object (1)>, <Band: Band object (2)>, <Band: Band object (3)>, <Band: Band object (4)>, <Band: Band object (5)>, <Band: Band object (6)>, <Band: Band
#  object (7)>, <Band: Band object (8)>, <Band: Band object (9)>, <Band: Band object (11)>, <Band: Band object (12)>, <Band: Band object (13)>, <Band: Band object (14)>, <Band: Band
# object (15)>, <Band: Band object (16)>]>
# In [6]: Band.objects.all()[3].name
# Out[6]: 'Pink Floyd'
#
# In [12]: # Posortuj je alfabetycznie.
# In [13]: Band.objects.all().order_by('name')
# Out[13]: <QuerySet [<Band: Band object (7)>, <Band: Band object (9)>, <Band: Band object (5)>, <Band: Band object (13)>, <Band: Band object (15)>, <Band: Band object (3)>, <Band: B
# and object (8)>, <Band: Band object (16)>, <Band: Band object (4)>, <Band: Band object (11)>, <Band: Band object (12)>, <Band: Band object (1)>, <Band: Band object (6)>, <Band: Ban
# d object (2)>, <Band: Band object (14)>]>
# In [14]: Band.objects.all().order_by('-name')
# Out[14]: <QuerySet [<Band: Band object (14)>, <Band: Band object (2)>, <Band: Band object (6)>, <Band: Band object (1)>, <Band: Band object (12)>, <Band: Band object (11)>, <Band:
# Band object (4)>, <Band: Band object (16)>, <Band: Band object (8)>, <Band: Band object (3)>, <Band: Band object (15)>, <Band: Band object (13)>, <Band: Band object (5)>, <Band: Ba
# nd object (9)>, <Band: Band object (7)>]>
# In [15]: Band.objects.all().order_by('-name', 'year')
# Out[15]: <QuerySet [<Band: Band object (14)>, <Band: Band object (2)>, <Band: Band object (6)>, <Band: Band object (1)>, <Band: Band object (12)>, <Band: Band object (11)>, <Band:
# Band object (4)>, <Band: Band object (16)>, <Band: Band object (8)>, <Band: Band object (3)>, <Band: Band object (15)>, <Band: Band object (13)>, <Band: Band object (5)>, <Band: Ba
# nd object (9)>, <Band: Band object (7)>]>
# In [16]: Band.objects.all().order_by('year', 'name')
# Out[16]: <QuerySet [<Band: Band object (5)>, <Band: Band object (13)>, <Band: Band object (1)>, <Band: Band object (2)>, <Band: Band object (4)>, <Band: Band object (7)>, <Band: Ba
# nd object (6)>, <Band: Band object (3)>, <Band: Band object (11)>, <Band: Band object (8)>, <Band: Band object (9)>, <Band: Band object (16)>, <Band: Band object (12)>, <Band: Band
#  object (14)>, <Band: Band object (15)>]>
#
# In [18]: Band.objects.all()
# Out[18]: <QuerySet [<Band: Band object (1)>, <Band: Band object (2)>, <Band: Band object (3)>, <Band: Band object (4)>, <Band: Band object (5)>, <Band: Band object (6)>, <Band: Ban
# d object (7)>, <Band: Band object (8)>, <Band: Band object (9)>, <Band: Band object (11)>, <Band: Band object (12)>, <Band: Band object (13)>, <Band: Band object (14)>, <Band: Band
#  object (15)>, <Band: Band object (16)>]>
# In [19]: Band.objects.all()[3]
# Out[19]: <Band: Band object (4)>
# In [20]: Band.objects.all()[3].name
# Out[20]: 'Pink Floyd'

# In [10]: # Dodaj dane zespołu Rage Against The Machine, rok założenia 1991.
# In [11]: Band.objects.create(name='Rage Against The Machine', year=1991, genre=0)
# Out[11]: Rage Against The Machine - 1991
#LUB
# In [12]: band = Band()
# In [13]: band.name = 'Five Finger Death Punch'
# In [14]: band.year = 1998
# In [15]: band.genre = 1
# In [16]: band.save()


#Znajdź wszystkie zespoły, które nie mają zdefinowanego roku założenia. Wypisz w konsoli ich nazwy i identyfikator nadany przez bazę danych.
# ZADANIE 2
#from exercises_app.models import Band



# In [3]: bands = Band.objects.filter(year=None)
# In [4]: bands
# Out[4]: <QuerySet [The Beatles - None, The Rolling Stones - None, Deep Purple - None, Dire Straits - None]>
# In [5]: for band in bands:
#    ...:     print(band.id, band.name)
#    ...:
# 1 The Beatles
# 2 The Rolling Stones
# 5 Deep Purple
# 13 Dire Straits
# In [9]: band_dict = Band.objects.filter(year=None).values('id', 'name')
# In [10]: for dictionary in band_dict:
#     ...:     print(dictionary['id'], dictionary['name'])
#     ...:
# 1 The Beatles
# 2 The Rolling Stones
# 5 Deep Purple
# 13 Dire Straits


#ZADANIE2 10:55 godzina
#Znajdź informacje o zespołach, które nie mają w naszej bazie podanego roku założenia. Uzupełnij informacje (może być losowo) i zapisz je w bazie danych.
# utworzenie foeru management w appce i pliku __init__, w management utworzeni folderu commands a w nim __init__ oraz pliku(random_band_year.py) ze skryptem:
# import random
#
# from django.core.management import BaseCommand
# from exercises_app.models import Band
#
#
# class Command(BaseCommand):
#     help = "Randomize Band year."
#
#     def _get_all_bands_without_year(self):
#         return Band.objects.filter(year=None)
#
#     @staticmethod
#     def _update_band_without_year(bands_without_year):
#         for band in bands_without_year:
#             print(f"Update band {band.name}")
#             band.year = random.randint(1970, 2021)
#             band.save()
#
#     def handle(self, *args, **options):
#         print("Starting band update.")
#         bands_without_year = self._get_all_bands_without_year()
#         print(f"Found bands {bands_without_year}")
#         self._update_band_without_year(bands_without_year)
#         print("Done!")



#####################   WYWOLANIE W SHELLu: python manage.py random_band_year   #https://docs.djangoproject.com/en/dev/howto/custom-management-commands/
#ZADANIE 3
        ######WOJTEK ROZWAIZANIE##########
#
# import random
#
# from django.core.management import BaseCommand
# from exercises_app.models import Band, GENRE_CHOICE
#
#
# class Command(BaseCommand):
#     help = "Random fill for Band genre and still active fields."
#
#     def handle(self, *args, **options):
#         print(self.help)
#         bands = Band.objects.all()
#         for band in bands:
#             band.genre = random.choice(GENRE_CHOICE)[0] # (1, 'Rock')[0]
#             band.still_active = random.choice([True, False])
#             band.save()
#         print('Done!')


#Pełna lista filtrów:
#https://docs.djangoproject.com/en/3.0/topics/db/queries/#retrieving-specific-objects-with-filters
#ZADANIE 4
# Znajdź i wypisz na konsoli wszystkie zespoły, które:
#


#from exercises_app.models import Band
# band = Band.objects.all().filter(name__contains='The') lub #band = Band.objects.all().filter(name__icontains='The')
#     Mają w nazwie "The",
# In [6]: Band.objects.filter(name__contains='The')
# Out[6]: <QuerySet [The Beatles - 2016, The Rolling Stones - 2016, The Clash - 1976, Rage Against The Machine - 1999]>
# In [7]: Band.objects.filter(name__icontains='The')
# Out[7]: <QuerySet [The Beatles - 2016, The Rolling Stones - 2016, The Clash - 1976, Rage Against The Machine - 1999]>
# #     założone zostały w latach 1980-tych i są wciąż aktywne,
# In [9]: Band.objects.filter(year__gte=1980, year__lte=1989, still_active=True)
# Out[9]: <QuerySet [Red Hot Chili Peppers - 1983]>
# #     założone zostały w latach 1970-tych oraz mają w nazwie "The",
# In [11]: Band.objects.filter(year__range=(1970, 1979), name__contains='The')
# Out[11]: <QuerySet [The Clash - 1970]>
# #     założone zostały w latach 1980-tych, oraz są już nieaktywne.
# In [13]: Band.objects.filter(year__range=(1980, 1989), still_active=False)
# Out[13]: <QuerySet [Metallica - 1988, Nirvana - 1987]>




#ZADANIE 5
    # Do modelu Category z poprzedniej części, dodaj kilka wybranych kategorii,

#Nie dodawaj tytułu ani zawartości losowo, skorzystaj z http://randomtextgenerator.com/

    # Category.objects.create(name="metal", description="Trzy nowo toż nosy się list. Nowe rozmaitością Ogon barbarzyństwa ramy Panu koń dnie gospodarskiéj moje. Ubrana Dawano śród chwali miasta B")
    # Category.objects.create(name="rock", description="Było bezprzykładną cicho myśl kusym Przedstawiając. Ryków wstał wspólni Nagła żywą mnicha dziécie grzeczne wyboru zabije. ")
    # Category.objects.create(name="trance", description="wierciadeł wyjeżdżali daje Mickiewiczem nosi fajt jako nuda przeznaczono najwyższych lewo Okna lity. Przeprosiwszy witać")
    # Category.objects.create(name="trance", description="Ryków wstał wspólni Nagła żywą mnicha dziécie grzeczne wyboru zabije. ")
    # Category.objects.create(name="pop", description="Pali Dojeżdżaczowi spod nami kula pary rosciągnionemi pokrewieństwem marszałkowską okna najwymowniejsza zwierciadlanéj Wiem Pyta.")
    #
    # # Dodaj kilka artykułów do modelu Article.
    #
    # Article.objects.create(title=" ", author="", content="", date_added="", status="", start_date="", end_date="")
    # Article.objects.create(title=" ", author="", content="", date_added="", status="", start_date="", end_date="")
    # Article.objects.create(title=" ", author="", content="", date_added="", status="", start_date="", end_date="")
    # Article.objects.create(title=" ", author="", content="", date_added="", status="", start_date="", end_date="")
    # Article.objects.create(title=" ", author="", content="", date_added="", status="", start_date="", end_date="")






#RELACJE###########################RELACJE###########################RELACJE###########################RELACJE###########################RELACJE###########################RELACJE########################
# ###RELACJE###########################RELACJE###########################RELACJE###########################RELACJE###########################RELACJE##########################

#ZADANIE1 RELACJA JEDNE DO WIELU 15:00 godzina

# class Album(models.Model):
#     title = models.CharField(max_length=128)
#     year = models.IntegerField()
#     rate = models.IntegerField(choices=RATE_CHOICE, default=0)
#     band = models.ForeignKey(Band, on_delete=models.CASCADE)  #ZADANIE1 RELACJA JEDNE DO WIELU 15:00 godzina

# Zadanie 2
#
# Dodaj do modeli kolejny: Song. Powinien mieć następujące pola:
#
#     title: string, max długość 128 znaków,
#     duration: czas (TimeField), może przyjmować null,
#     dodaj relację wiele-do-jednego tak, aby jeden album mógł mieć wiele piosenek.
#
# Uzupełnij dane, tworząc albumy grup i uzupełniając je piosenkami (nie przejmuj się, czy piosenki są prawdziwe, po prostu je dodaj).



#ZADANIE3
    # Wyswietl wszystkie albumy dowolnego zespołu,
# from exercises_app.models import Album, Song
#
# albums = Album.objects.filter(band_id=4)
# In [27]: songs = Song.objects.filter(album_id=4)
#
#lub
# band = Band.objects.get(pk=5)
# band.album_set.all()




#Wyswietl wszystkie piosenki z każdego albumu.

# In [10]: albums = Album.objects.filter(band=band)
# In [11]: albums
# Out[11]: <QuerySet [<Album: Album object (14)>, <Album: Album object (68)>, <Album: Album object (69)>, <Album: Album object (70)>, <Album: Album object (71)>, <Album: Album object
#  (72)>]>
# In [13]: for album in albums:
#     ...:     print(f"Piosenki albumu {album.title}")
#     ...:     print(Song.objects.filter(album=album))
#     ...:     input()
#     ...:
# Piosenki albumu Southern between before lead.
# <QuerySet [<Song: Song object (40)>]>
# Piosenki albumu Stand maintain court face.
# <QuerySet [<Song: Song object (208)>, <Song: Song object (209)>]>
# Piosenki albumu Discover near investment before. Leader phone father education customer fear major.
# Eight lead institution.
# <QuerySet [<Song: Song object (210)>, <Song: Song object (211)>]>
# Piosenki albumu West large each say science international.
# <QuerySet [<Song: Song object (212)>, <Song: Song object (213)>]>
# Piosenki albumu Reduce prevent do.
# <QuerySet [<Song: Song object (214)>]>
# Piosenki albumu Indeed kind win store.
# <QuerySet [<Song: Song object (215)>]>

#LUB SKRYPT COMMANDS:
# from django.core.management import BaseCommand
#
# from exercises_app.models import Band, Album, Song
#
#
# class Command(BaseCommand):
#     help = "Create some random albums."
#
#     def handle(self, *args, **options):
#         band = Band.objects.get(pk=5)
#         albums = Album.objects.filter(band=band) # band.album_set.all()
#         print(f"Zespół {band.name}")
#         for album in albums:
#             print(f'Album {album.title}')
#             songs = Song.objects.filter(album=album) # album.song_set.all()
#             i = 0
#             for song in songs:
#                 i += 1
#                 print(f"{i} - {song.title}")




# ZADANIE 5  QUERY WYLISTOWANIE Z RELACJI WIELE DO WIELU DANEJ KATEGORII
    #Wybierz kategorię. Następnie wybierz (i wypisz na konsoli) wszystkie artykuły należące do tej kategorii.
    



#q = Category.objects.get(id=1).article_set.all().values('id', 'title') #z relacji wiele do wielu, pobiera id kategorii i wyswietla wszystkie artykuly z danej kategorii 

#In [156]: q
#Out[156]: <QuerySet [{'id': 1, 'title': 'Pattern dream.'}, {'id': 2, 'title': 'Travel.'}, {'id': 3, 'title': 'Structure have.'}, {'id': 5, 'title': 'Culture fine it.'}, {'id': 6, 'title': 'Go poor I citizen.'}]>


#LUB
# In [170]: q = Article.objects.filter(categories__id=1).values('id','title')
# In [171]: q
# Out[171]: <QuerySet [{'id': 1, 'title': 'Pattern dream.'}, {'id': 2, 'title': 'Travel.'}, {'id': 3, 'title': 'Structure have.'}, {'id': 5, 'title': 'Culture fine it.'}, {'id': 6, 'title': 'Go poor I citizen.'}]>

#LUB Artykul o id 2 jest przypisany do categorii id i name
#In [193]: q = Category.objects.filter(article__id=2).values('id','name')

#In [194]: q
#Out[194]: <QuerySet [{'id': 1, 'name': 'metal'}, {'id': 4, 'name': 'food'}, {'id': 5, 'name': 'people'}]>


#Wybierz dwie kategorie. Następnie wybierz i wypisz na konsoli wszystkie artykuły należące jednocześnie do obu kategorii:

#In [244]: q = Article.objects.filter(categories__in=[1,2]).values('id', 'title')  lub q = Article.objects.filter(categories__id__in=[1,2]).values('id','title')


#In [245]: q
#Out[245]: <QuerySet [{'id': 1, 'title': 'Pattern dream.'}, {'id': 1, 'title': 'Pattern dream.'}, {'id': 2, 'title': 'Travel.'}, {'id': 3, 'title': 'Structure have.'}, {'id': 3, 'title': 'Structure have.'}, {'id': 4, 'title': 'Close site.'}, {'id': 5, 'title': 'Culture fine it.'}, {'id': 6, 'title': 'Go poor I citizen.'}]>


#LUB
#from django.db.models import Q

#In [263]: q = Article.objects.filter(Q(categories=1) | Q(categories=2)).values('id','title')

#In [264]: q
#Out[264]: <QuerySet [{'id': 1, 'title': 'Pattern dream.'}, {'id': 1, 'title': 'Pattern dream.'}, {'id': 2, 'title': 'Travel.'}, {'id': 3, 'title': 'Structure have.'}, {'id': 3, 'title': 'Structure have.'}, {'id': 4, 'title': 'Close site.'}, {'id': 5, 'title': 'Culture fine it.'}, {'id': 6, 'title': 'Go poor I citizen.'}]>


#LUB Artykuly o id 1 i 2 sa przypisane do kategorii 1,2,4,5,7 
#In [276]: q = Category.objects.filter(Q(article__id=1) | Q(article__id=2)).values('id','name')

#In [277]: q
#Out[277]: <QuerySet [{'id': 1, 'name': 'metal'}, {'id': 1, 'name': 'metal'}, {'id': 2, 'name': 'sport'}, {'id': 4, 'name': 'food'}, {'id': 4, 'name': 'food'}, {'id': 5, 'name': 'people'}, {'id': 7, 'name': 'IT'}]>


#DODAWANIE DO TABELI MANY TO FIELD WARTOSCI
# In [19]: m = Movie.objects.get(id=1)

# In [20]: g = Genre.objects.get(name='adventure')

# In [21]: m.genre.set([g])
