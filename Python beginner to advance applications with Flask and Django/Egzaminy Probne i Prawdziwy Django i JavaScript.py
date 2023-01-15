 WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO views WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO 
  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO 
   WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO  WARSZTAT PYTHON DJANGO 



models.py



from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.TextField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector = models.BooleanField()

class RoomBooking(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)


class Meta:
   unique_together = ('room_id', 'date',)


   urls.py



from django.contrib import admin
from django.urls import path

#APPLICTIONS
from booking_rooms.views import AddRoom, MainMenu, DeleteRoom, ModifyRoom, BookRoom, Search

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main-menu-rooms', MainMenu.as_view()),
    path('room/new',  AddRoom.as_view()),
    path('room/delete/<int:room_id>', DeleteRoom.as_view()),
    path('room/modify/<int:room_id>', ModifyRoom.as_view()),
    path('room/reserve/<int:room_id>', BookRoom.as_view()),
    path('search/', Search.as_view())

]






views.py


from datetime import datetime, date

from django.contrib import messages

from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from booking_rooms.models import Room, RoomBooking


#MAIN MENU ROOM
#VIEW ROOMS
class MainMenu(View):
    def get(self, request):
        rooms = Room.objects.all()
        bookedrooms = RoomBooking.objects.all().order_by('date')

        current_date = date.today()
        # current_date = datetime.date.today()
        # for room in rooms:
        #     for bookedroom in bookedrooms:
        #         if current_date == bookedroom.date and room.id == bookedroom.room_id_id:
        #             available = 'Yes'
        #         else:
        #             available = 'No'


        return render(request, 'booking_rooms_templates/main_menu_booking_rooms_html.html',
                      context={'rooms': rooms, 'bookedrooms': bookedrooms, 'current_date': current_date})



#ADDING NEW ROOMS FORM INTO DATABASE
class AddRoom(View):
    def get(self, request):

        #ADD ROOM FORM
        return render(request, 'booking_rooms_templates/add_room_html.html')



    def post(self, request):

        room_name = request.POST.get('room_name')
        room_capacity = request.POST.get('room_capacity')
        room_projector = request.POST.get('room_projector')

        #ROOM VALIDATE IS EXIST IN DATABASE
        if Room.objects.filter(name=room_name).first():
            error_name = f"That room exist: {room_name}"
            return render(request, 'booking_rooms_templates/add_room_html.html', context={'error_name': error_name})

        #ROOM FILL NAME/CAPACITY VALIDATION
        if room_name == '' or room_capacity == '':
            error_name = "No provided name or/and capacity, please try again"
            return render(request, 'booking_rooms_templates/add_room_html.html', context={'error_name': error_name})


        #SET PROJECTOR: FALSE TRUE BY CHECKBOX TYPE 'ON' 'OFF'
        if room_projector == 'on':
            room_projector = True
        else:
            room_projector = False

        #ROOM CAPACITY VALIDATION
        if int(room_capacity) <= 0:
            error_capacity = "Wrong capacity number (only integer and greater than 0, please try again"
            return render(request, 'booking_rooms_templates/add_room_html.html', context={'error_name': error_capacity})

        #ROOM ADD TO DATABASE
        Room.objects.create(name=room_name, capacity=room_capacity, projector=room_projector)
        #room = Room(name=room_name, capacity=room_capacity, projector=room_projector)
        #room.save()

        return redirect('/main-menu-rooms')


#DELETE ROOM
class DeleteRoom(View):
    def get(self, request, room_id):

        room_del = Room.objects.get(id=room_id)
        room_del.delete()

        #MESSAGE AFTER DELETE ROOM FROM DATABASE IN MAIN MENU
        messages.add_message(request, messages.INFO, f'Room {room_del.name} has been deleted')
        return redirect('/main-menu-rooms')

class ModifyRoom(View):
    def get(self, request, room_id):
        room_mod = Room.objects.get(id=room_id)


        return render(request, 'booking_rooms_templates/modify_room_html.html', context={'room_mod': room_mod})

    def post(self, request, room_id):

        room_name = request.POST.get('room_name')
        room_capacity = request.POST.get('room_capacity')
        room_projector = request.POST.get('room_projector')


        #ROOM FILL NAME/CAPACITY VALIDATION
        if room_name == '' or room_capacity == '':
            error_name = "No provided name or/and capacity, please try again"
            return render(request, 'booking_rooms_templates/modify_room_html.html', context={'error_name': error_name})
        # ROOM VALIDATE IS EXIST IN DATABASE
        if Room.objects.filter(name=room_name).first():
            error_name = f"That room exist: {room_name}, provide another"
            return render(request, 'booking_rooms_templates/modify_room_html.html', context={'error_name': error_name})

        #SET PROJECTOR: FALSE TRUE BY CHECKBOX TYPE 'ON' 'OFF'
        if room_projector == 'on':
            room_projector = True
        else:
            room_projector = False

        #ROOM CAPACITY VALIDATION
        if int(room_capacity) <= 0:
            error_capacity = "Wrong capacity number (only integer and greater than 0, please try again"
            return render(request, 'booking_rooms_templates/modify_room_html.html', context={'error_name': error_capacity})

        #ROOM MODIFY BY ROOM_ID TO DATABASE
        room = Room(id=room_id, name=room_name, capacity=room_capacity, projector=room_projector)
        room.save()

        return redirect('/main-menu-rooms')

class BookRoom(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=room_id)
        bookedrooms = RoomBooking.objects.filter(room_id=room_id)


        return render(request, 'booking_rooms_templates/booking_room_html.html',
                      context={'room': room, 'bookedrooms': bookedrooms})


    def post(self, request, room_id):

        room = Room.objects.get(id=room_id)

        room_book_date = request.POST.get('room_book_date')
        comment = request.POST.get('comment')

        if room_book_date < str(datetime.today()):
            error_date = "Wrong data - from past, please try again"
            return render(request, 'booking_rooms_templates/booking_room_html.html',
                          context={'room': room, 'error_date': error_date})


        if RoomBooking.objects.filter(room_id_id=room, date=room_book_date):
            error_date = "Room already booked this date, please try again"
            return render(request, 'booking_rooms_templates/booking_room_html.html',
                          context={'room': room, 'error_date': error_date})


        RoomBooking.objects.create(room_id_id=room_id, date=room_book_date, comment=comment)

        return redirect('/main-menu-rooms')


class Search(View):
    def get(self, request):


        current_date = str(datetime.today().strftime('%B %d, %Y'))

        rooms = Room.objects.all()


        room_name = request.GET.get('room_name')
        room_capacity = request.GET.get('room_capacity')
        room_projector = request.GET.get('room_projector')

        # SET PROJECTOR: FALSE or TRUE BY CHECKBOX TYPE 'ON' 'OFF'
        if room_projector == 'on':
            room_projector = True
        else:
            room_projector = False


        if room_capacity == '':
            room_capacity = 0

        #QUERY FILTERS BY NAME CAPACITY PROJECTOR AVAILABLE
        #icontains checking by upper and lower cases
        rooms = rooms.filter(name__icontains=room_name)
        rooms = rooms.filter(capacity__gt=room_capacity)
        rooms = rooms.filter(projector=room_projector)

        bookedrooms = RoomBooking.objects.all().order_by('date')


        return render(request, 'booking_rooms_templates/main_menu_booking_rooms_html.html',
                      context={'rooms': rooms, 'bookedrooms': bookedrooms, 'current_date': current_date})




 







EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO 
EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO 
EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO EGZAMIN PYTHON DJANGO 
EGZAMIN PYTHON DJANGO 
    #############################################################################################
urls.py
"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from exam_app.views import lecture_details, set_username, delete_cookie, \
    CreateCookieView, IndexView, say_hello, AddStudent

# SayHelloView ,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('lecture_details/<int:lecture_id>/', lecture_details),
    path('set_username/<str:user_name>/', set_username),

    # path('say_hello/<int:n>/', SayHelloView.as_view()),
    # path('say_hello/', SayHelloView.as_view()),
    path('say_hello/', say_hello),
    path('say_hello/<int:n>/', say_hello),


    # path('create_cookie/<cookie_name>/<cookie_value>/<int:cookie_time>', CreateCookieView.as_view()),
    re_path(r'^create_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/(?P<cookie_value>[a-zA-Z0-9]+)/(?P<cookie_time>\d+)/$', CreateCookieView.as_view()),

    path('delete_cookie/<cookie_name>/', delete_cookie),
    path('add_student/', AddStudent.as_view()),

]


models.py


from django.db import models
from django.db.models import ManyToManyField   #relacja wiele do wielu

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64)
    year_at_university = models.IntegerField()
    is_active = models.BooleanField(default=True)


class Lecture(models.Model):
    name = models.CharField(max_length=128)
    lecturer = models.CharField(max_length=64)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    stdent = models.ManyToManyField(Student)




views.py



from django.http import HttpResponse
from django.shortcuts import render
from django.utils import html
from django.template import loader

from django.views import View


from exam_app.models import Lecture
from exam_app.models import Student

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, "HTML.html")



def lecture_details(request, lecture_id):
    lecture = Lecture.objects.get(id=lecture_id)



    if request.method == "GET":


        return render(
            request, 'lecture_details.html', context={"lecture": lecture})



def set_username(request, user_name):
    request.session["user_name"] = user_name

    return HttpResponse("Zapisano dane " + user_name)


# class SayHelloView(View):
#     def get(self, request, n=10):
#         user_name = request.session.get("user_name")
#
#         if not user_name:
#             return HttpResponse('<p>Witaj nieznajomy</p>' * n)
#
#         return HttpResponse(n * f'<p>{user_name}</p>')

def say_hello(request, n=10):
        user_name = request.session.get("user_name")

        if not user_name:
            return HttpResponse('<p>Witaj nieznajomy</p>' * n)

        return HttpResponse(n * f'<p>{user_name}</p>')



class CreateCookieView(View):
    def get(self, request, cookie_name, cookie_value, cookie_time):
        response = HttpResponse("ciastko ustawione")
        response.set_cookie(cookie_name, cookie_value, max_age=int(cookie_time) * 60)
        return response


def delete_cookie(request, cookie_name):

    cookie = request.COOKIES.get(cookie_name)


    if not cookie:
        return HttpResponse("Brak takiego ciasteczka")

    response = HttpResponse("Deleted cookie = " + cookie_name + ' : ' + cookie   )
    response.delete_cookie(cookie_name)
    return response


class AddStudent(View):
    def get(self, request):
        # teams = Team.objects.all()

        ######3 #Pobieranie danych z sesji#########
        # if request.session.items():
        # game_values_session = request.session.items()
        # team_home_id = request.session.get('team_home')

        return render(
            request, 'add_student.html')





    def post(self, request):




        name = request.POST.get("student_name")
        year_at_university = request.POST.get("year_at_university")
        is_active = request.POST.get("is_active")

        if is_active == 'on':
            is_active = True
        else:
            is_active = False


        student = Student(name=name, year_at_university=year_at_university, is_active=is_active)
        # Student.objects.create(name=name, year_at_university=year_at_university, is_active=is_active)
        # stworzenie studenta wraz z zapisem (od razu przy pomocy create)
        student.save()



        success = "Dodano studenta:"


        return render(request, 'add_student.html',
                      context={
                                'student_name': student_name, 'year_at_university': year_at_university, 'success': success,  #added html


                           })



# Zadanie 4 – widoki – rozwiązanie
#
# Zacznijmy od utworzenia widoków. No końcu dodamy je do pliku urls.py. Ponieważ zwracać będziemy proste napisy, pominiemy tutaj szablony. Będziemy zwracać kod HTML bezpośrednio z kodu Pythona.
# Zapisanie użytkownika do sesji
#
# W tym widoku, musimy przechwycić parametr z adresu URL i zapisać go do sesji. Sesję znajdziemy w obiekcie request.
# Przykład:
#
# from django.http import HttpResponse
#
# from django.views import View
#
#
# ...
#
#
# class SetUsernameView(View):
#
#     def get(self, request, user_name):
#
#         request.session["user_name"] = user_name
#
#         return HttpResponse("Zapisano dane")
#
#     class SetUsernameView(View): – tworzymy widok,
#     request.session["user_name"] = user_name – zapisujemy użytkownika do sesji,
#     return HttpResponse("Zapisano dane") – zwracamy komunikat bezpośrednio z pominięciem szablonu.
#
# Say Hello
#
# Widok powinien przyjąć jeden parametr – n. Następnie sprawdzamy, czy użytkownik jest zapisany w sesji i na tej podstawie zwracamy odpowiedni komunikat.
# Przykład:
#
# from django.http import HttpResponse
#
# from django.views import View
#
#
# ...
#
#
# class SayHelloView(View):
#
#     def get(self, request, n=10):
#
#         user_name = request.session.get("user_name")
#
#         if not user_name:
#
#             return HttpResponse('<p>Witaj nieznajomy</p>' * n)
#
#         return HttpResponse(n * f'<p>{user_name}</p>')
#
#     def get(self, request, n=10): – parametrowi n ustawiamy domyślną wartość. Dzięki temu, odpowiednio ustawiając adresy URL, obsłużymy oba podpunkty jednym widokiem.
#     user_name = request.session.get("user_name") – pobieramy użytkownika z sesji wykorzystując metodę get. Dzięki temu przy braku wartości dostaniemy None, zamiast błędu KeyError.
#     if not user_name: – jeśli użytkownik nie jest ustawiony w sesji, zwracamy odpowiedni komunikat.
#     return HttpResponse(n * f'<p>{user_name}</p>') – użyliśmy paragrafów, żeby komunikaty wyświetliły się w nowych liniach.
#
# Utworzenie ciasteczka
#
# Utwórzmy teraz widok, który zapisze ciasteczko. W adresie URL musimy ustawić aż 3 parametry.
# Przykład:
#
# from django.http import HttpResponse
#
# from django.views import View
#
#
# ...
#
#
# class CreateCookieView(View):
#
#     def get(self, request, cookie_name, cookie_value, cookie_time):
#
#         response = HttpResponse("ciastko ustawione")
#
#         response.set_cookie(cookie_name, cookie_value, max_age=int(cookie_time) * 60)
#
#         return response
#
#     def get(self, request, cookie_name, cookie_value, cookie_time): – przekazujemy 3 parametry.
#     response = HttpResponse("ciastko ustawione") – ponieważ ciasteczko musimy dodać do odpowiedzi, musimy utworzyć ją wcześniej.
#     response.set_cookie(cookie_name, cookie_value, max_age=int(cookie_time) * 60) – dodajemy ciastko, czas musimy zrzutować na int i pomnożyć przez 60 (mamy podany czas w minutach, a ustawiamy go w sekundach). Nie przejmujemy się walidacją, bo zrobimy to odpowiednim wyrażeniem regularnym w adresie URL.
#
# Usuwanie ciasteczka
#
# Na koniec musimy dodać widok, który usunie nam ciasteczko. Ponieważ chcemy je wyświetlić, powinniśmy je pobrać, przed usunięciem.
# Przykład:
#
# from django.http import HttpResponse
#
# from django.views import View
#
#
# ...
#
#
# class DeleteCookieView(View):
#
#     def get(self, request, cookie_name):
#
#         cookie = request.COOKIES.get(cookie_name)
#
#         if not cookie:
#
#             return HttpResponse("Brak takiego ciasteczka")
#
#         response = HttpResponse(f"Ciasteczko {cookie_name}:{cookie} zostało usunięte")
#
#         response.delete_cookie(cookie_name)
#
#         return response
#
#     cookie = request.COOKIES.get(cookie_name) – pobieramy wartość ciasteczka, korzystając z metody get. Jeśli ciasteczko o podanej nazwie, nie jest zapisane, dostaniemy None.
#     if not cookie: – jeśli nie ma ciasteczka, wyświetlamy odpowiedni komunikat.
#     response = HttpResponse(f"Ciasteczko {cookie_name}:{cookie} zostało usunięte") – ciasteczko usuwamy z odpowiedzi, dlatego musimy utworzyć ją wcześniej.
#     response.delete_cookie(cookie_name) – do usunięcia ciasteczka używamy metody delete_cookie.
#     return response – zwracamy odpowiedź.
#
# Adresy URL
#
# Teraz, musimy dodać nasze widoki do pliku urls.py, przyporządkowując im odpowiednie adresy URL. Aby dokonać walidacji, wykorzystamy metodę re_path, oraz wyrażenia regularne.
# Przykład:
#
# from django.contrib import admin
#
# from django.urls import path, re_path
#
# from exam_app.views import SetUsernameView, SayHelloView,\
#
#     CreateCookieView, DeleteCookieView
#
#
# urlpatterns = [
#
#     path('admin/', admin.site.urls),
#
#
#     ...
#
#
#     re_path(r'^set_username/(?P<user_name>[a-zA-Z0-9]+)/$', SetUsernameView.as_view()),
#
#     path('say_hello/<int:n>/', SayHelloView.as_view()),
#
#     path('say_hello/', SayHelloView.as_view()),
#
#     re_path(r'^create_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/(?P<cookie_value>[a-zA-Z0-9]+)/(?P<cookie_time>\d+)/$',
#
#             CreateCookieView.as_view()),
#
#     re_path(r'^delete_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/$', DeleteCookieView.as_view()),
#
# ]
#
#     re_path(r'^set_username/(?P<user_name>[a-zA-Z0-9]+)/$', SetUsernameView.as_view()), – nazwa może składać się tylko z liter i cyfr: [a-zA-Z0-9]+, przypisujemy ją do zmiennej user_name.
#     path('say_hello/<int:n>/', SayHelloView.as_view()), – tutaj możemy zastosować route zaznaczając, że spodziewamy się typu int.
#     path('say_hello/', SayHelloView.as_view()), – ponieważ parametr ustawiliśmy jako opcjonalny, z domyślną wartością 10, możemy wykorzystać ten sam widok w dwóch miejscach.
#     re_path(r'^create_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/(?P<cookie_value>[a-zA-Z0-9]+)/(?P<cookie_time>\d+)/$', – nazwa i wartość ciasteczka powinny składać się z liter i cyfr: [a-zA-Z0-9]+, czas życia ciasteczka to liczba: \d+.
#     re_path(r'^delete_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/$', DeleteCookieView.as_view()), – nazwa ciasteczka ma te same ograniczenia, co w poprzednim widoku.




lecture_details.html


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lecture Details</title>
</head>
<body>
<h1>Nazwa wykładu: {{ lecture.name }}</h1>
<h2>Wykładowca: {{ lecture.lecturer }}</h2>
<h3>Studenci</h3>
<ul>

  {% for student in lecture.stdent.all %}

    <li>{{ student.name }}</li>

  {% endfor %}



</ul>
</body>
</html>


add_student.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ADD STUDENT</title>
</head>
<body>

<form action="" method="POST">
  {% csrf_token %}
<br>

   <b>Imie studenta:</b> <input type="text" name="student_name" >
   <b>Rok na uniwerku:</b> <input type="number"  name="year_at_university" >
   <b>Aktywny?:</b> <input type="checkbox" name="is_active" >



  <input type="submit" value="Dodaj studenta">
</form>
<br>
{{ success }}  {{ student_name }} {{ year_at_university }}
</body>
</html>













EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT 
EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT 
EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT EGZAMIN JAVASCRIPT 




// Zadanie1
// Nie używajcie eventu DOMContentLoaded. Skrypt jest wczytany do pliku html przed końcem body.
// Napiszcie funkcję o nazwie concatArray(array1, array2), która przyjmuje jako parametry dwie tablice.
// Niech funkcja ta zwraca nową tablicę będącą połączeniem tych dwóch.


function concatArray(array1, array2){
   return array1.concat(array2) 
}


concatArray( [1,3],[3,5] );
console.log(concatArray( [1,3],[3,5] ));
 

 








// Zadanie 2

// Używając JavaScript dopiszcie do wszystkich divów o klasie color nasłuchiwanie zdarzeń, 
// które po najechaniu na element sprawi, że kolor diva zmieni się na losowy, a na divie pokaże się 
// tekst trzymany w data-text.
// Zjechanie z diva powinno usuwać tekst, ale div powinien zostać pokolorowany.
// Ponowne najechanie powinno zmienić kolor tła i znowu wyświetlić tekst.
// Hint: Żeby uzyskać losowy kolor użyj poniższego kodu:
// let randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Zadanie 2</title>
    <script type="text/JavaScript" src="app.js"></script>
    <style>
        div {
            width: 120px;
            height: 100px;
            border: 2px solid black;
            border-radius: 10px;
            margin-bottom: 20px;
            
        }
    </style>
</head>
<body>
<div class='color' data-text="Hello, I'm div 1"></div>
<div class='color' data-text="Hello, I'm div 2"></div>
<div class='color' data-text="Hello, I'm div 3"></div>
<div class='color' data-text="Hello, I'm div 4"></div>
</body>
</html>



console.log("TEXT");
const colorDiv = document.querySelector('.color')
console.log(colorDiv);



document.addEventListener("DOMContentLoaded", function () {
    const divElems = document.querySelectorAll("div.color");
  
    
  
    divElems.forEach(function(el){ 
      el.addEventListener("mouseover", function(){
        this.innerText = this.dataset.text;
        this.style.backgroundColor = "#" + Math.floor(Math.random()*16777215).toString(16);
  
      });
  
  
      el.addEventListener("mouseout", event => {
        event.target.innerText = null;
  
      });
  
    });
  
  });
 





// Zadanie 3
// Zadanie

// W tym zadaniu możecie używać eventu DOMContentLoaded.
// Do wszystkich guzików znajdujących się na stronie dopiszcie event tak,
// aby po naciśnięciu przycisku w divie o id container pojawił się tekst trzymany w data-text.








<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h3> Tekst z atrybutu dataset z guzików powinien pojawiać się w tym kontenerze </h3>

<div id="container">  </div><br>

<button data-text="Tekst do guzika 1">Click me!</button>
<button data-text="Tekst do guzika 2">Click me!</button>
<button data-text="Tekst do guzika 3">Click me!</button>

</body>
</html>





document.addEventListener("DOMContentLoaded", function () {
    const buttonB = document.querySelectorAll("button");
    const cont = document.querySelector('#container')
    
  
    buttonB.forEach(function(el){ 
      el.addEventListener("click", function(){
        this.innerText = this.dataset.text;
        cont.innerText = this.dataset.text;
  
      });
  
  
   
    });
  
  });






// Zadanie 4

// W tym zadaniu możecie używać eventu DOMContentLoaded.

// Na stronie znajduje się lista zakupów.
// Popatrzcie na HTML i zobaczcie jak lista jest zbudowana.
// Dopiszcie odpowiednią obsługę eventów tak, aby:

//     po kliknięciu przycisku pierwszego do listy został dopisany nowy produkt - chleb.
//     po kliknięciu przycisku drugiego z listy był usuwany ostatni element.
//     po kliknięciu przycisku trzeciego na końcu listy był dodawany nowy produkt, który jest klonem drugiego produktu - o ile ten istnieje.




<!DOCTYPE html>
<html lang="pl-PL">
<head>
    <meta charset="UTF-8">
    <title>Zadanie 4</title>
 
    <script type="text/JavaScript" src="app.js"></script>
</head>
<body>

<h1>Lista zakupów</h1>

<div id="buttons">
    <button id="button-1">Przycisk 1</button>
    <button id="button-2">Przycisk 2</button>
    <button id="button-3">Przycisk 3</button>
</div>

<ul id="shopping-list">
    <li>
        Jajka
    </li>
    <li>
        Mąka
    </li>
    <li>
        Cukier
    </li>
</ul>
</body>
</html>








document.addEventListener("DOMContentLoaded", function() { 
const button1 = document.getElementById("button-1");
const button2 = document.getElementById("button-2");
const button3 = document.getElementById("button-3");

const list = document.querySelector('#shopping-list');

button1.addEventListener('click', function(){
     
    const listElement = document.createElement('li');
 
    // listElement.classList.add('list-group-item');
    listElement.innerText = `Chleb`;
    list.appendChild(listElement);

    })


button2.addEventListener('click', function(){
//const elemToDelete = shoppingList.lastElementChild;
    
    list.lastChild.remove();
    })

    button3.addEventListener("click", function () {

        if (list.children.length >= 2) {
    
          const clone = list.children[0].cloneNode(true);
    
          list.appendChild(clone);
    
        }
    
      });


})
  
 

Zadanie 5
 

Wasz sklep internetowy zajmuje się sprzedażą książek.
Wprowadzacie nowy produkt do oferty czyli ebooki.

Stworzenie klasy bazowej Stwórzcie klasę o nazwie Product.
Będzie to klasa, która w swoim konstruktorze powinna ustawiać takie dane jak

    title - tytuł produktu ,
    author - autor

Stworzenie obiektów
W związku z dodaniem do oferty nowego produktu - ebooka - stwórzcie dwie klasy dziedziczące po klasie bazowej:
-Ebook, -Book.

Utwórzcie te klasy w taki sposób, aby można było na ich podstawie stworzyć następujące obiekty:

    ebook pod tytułem Ciemniejsze niebo napisany przez Ruben Eliassen.
    książkę pod tytułem Najdłuższa noc napisaną przez Macieja Dancewicza.

Wyświetlanie informacji o produkcje

    W odpowiedniej klasie stwórzcie metodę printInfo().
    Do wyświetlanie wykorzystajcie ten szablon tekstu:
    ${this.constructor.name} - title: ${this.title}, author: ${this.author}

Zamawianie produktów
Wasi klienci chcą móc ściągać oraz zamawiać książki na podany adres.
Stwórzcie w odpowiednich klasach następujące metody:

    download - która wypisuje w konsoli tekst Ściąganie... [tutaj wstawcie tytuł]. Niech ten tekst również będzie zwracany przez metodę oprócz wypisania w konsoli.
    order - która wypisuje w konsoli tekst Podaj adres dostawy! Niech ten tekst również będzie zwracany przez metodę oprócz wypisania w konsoli.








class Product {
  constructor(title, author) {
    this.title = title;
    this.author = author;

  }
  printInfo() {
    console.log(`${this.constructor.name} - title: ${this.title}, author: ${this.author}`);
  }
}


class Book extends Product {
  order() {
    const text = 'Podaj adres dostawy!';
    console.log(text);
    return text;
  }
}


class Ebook extends Product {
  download() {
    const text = 'Ściąganie... ' + this.title;
    console.log(text);
    return text;
  }
}


const book = new Book('Najdłuższa noc', 'Maciej Dancewicz');
const ebook = new Ebook('Ciemniejsze niebo', 'Ruben Eliassen');


book.printInfo();
ebook.printInfo();

book.order();
ebook.download();



LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: 
LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: 
LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: LUB MOJE: 
 


class Product {
    constructor() {
        this.title = "Rubben Eliassen"
        this.author = "Rubben Eliassen"
        }

        printInfo() {
console.log(`${this.constructor.name} - title: ${this.title}, author: ${this.author}`)

return `${this.constructor.name} - title: ${this.title}, author: ${this.author}`
      }

download(){
console.log(`Sciaganie... ${this.title}`)
return `Sciaganie... ${this.title}`


} 

    }


    class Book extends Product {
        constructor() {
            super();


            this.title = "Ciemniejsze Niebo"
            this.author = "Rubben Eliassen"
            
        }
    }


    class EBook extends Product {
        constructor() {
        super();
        this.title = "11111"
        this.author = "222"
        }
    }


 const book = new Book( )
 const ebook = new EBook()


book.printInfo();
ebook.printInfo();

book.download();








// Zadanie 6

// Korzystając z adresu https://swapi.dev/api/starships wczytajcie na stronę informacje o statkach z Gwiezdnych Wojen.
// Kolejne statki wstawcie do listy.
// Nazwy statków wczytajcie do elementów h2, natomiast model do elementów h3.
// Utwórzcie te elementy i wstawcie je do DOM.
// Zauważcie, że dane nas interesujące znajdują się w tablicy, która znajduje się w jednym ze zwracanych w obiekcie atrybutów.

// Hint:
// Zobaczcie jak wygląda w konsoli obiekt, który otrzymujecie jako odpowiedź, zanim wstawicie content na stronę.


getData('https://swapi.dev/api/starships');


function getData(url) {

    fetch(url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            


 
            const tasks = data.results;
            console.log('Odpowiedź z serwera to:', data);
            console.log(`Dane data: ${data.results}`);
          

        
        
            console.log(`All DATA:`)
           
              
 
data.results.forEach(function(starship, index) {
    index++;
    console.log(`DATA ${index} `);
    
  console.log(starship)

});


           
             //console.log(task.results );
              
        
            });
        }





