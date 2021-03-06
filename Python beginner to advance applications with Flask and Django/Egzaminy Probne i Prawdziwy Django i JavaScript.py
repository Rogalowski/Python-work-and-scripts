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



# Zadanie 4 ??? widoki ??? rozwi??zanie
#
# Zacznijmy od utworzenia widok??w. No ko??cu dodamy je do pliku urls.py. Poniewa?? zwraca?? b??dziemy proste napisy, pominiemy tutaj szablony. B??dziemy zwraca?? kod HTML bezpo??rednio z kodu Pythona.
# Zapisanie u??ytkownika do sesji
#
# W tym widoku, musimy przechwyci?? parametr z adresu URL i zapisa?? go do sesji. Sesj?? znajdziemy w obiekcie request.
# Przyk??ad:
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
#     class SetUsernameView(View): ??? tworzymy widok,
#     request.session["user_name"] = user_name ??? zapisujemy u??ytkownika do sesji,
#     return HttpResponse("Zapisano dane") ??? zwracamy komunikat bezpo??rednio z pomini??ciem szablonu.
#
# Say Hello
#
# Widok powinien przyj???? jeden parametr ??? n. Nast??pnie sprawdzamy, czy u??ytkownik jest zapisany w sesji i na tej podstawie zwracamy odpowiedni komunikat.
# Przyk??ad:
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
#     def get(self, request, n=10): ??? parametrowi n ustawiamy domy??ln?? warto????. Dzi??ki temu, odpowiednio ustawiaj??c adresy URL, obs??u??ymy oba podpunkty jednym widokiem.
#     user_name = request.session.get("user_name") ??? pobieramy u??ytkownika z sesji wykorzystuj??c metod?? get. Dzi??ki temu przy braku warto??ci dostaniemy None, zamiast b????du KeyError.
#     if not user_name: ??? je??li u??ytkownik nie jest ustawiony w sesji, zwracamy odpowiedni komunikat.
#     return HttpResponse(n * f'<p>{user_name}</p>') ??? u??yli??my paragraf??w, ??eby komunikaty wy??wietli??y si?? w nowych liniach.
#
# Utworzenie ciasteczka
#
# Utw??rzmy teraz widok, kt??ry zapisze ciasteczko. W adresie URL musimy ustawi?? a?? 3 parametry.
# Przyk??ad:
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
#     def get(self, request, cookie_name, cookie_value, cookie_time): ??? przekazujemy 3 parametry.
#     response = HttpResponse("ciastko ustawione") ??? poniewa?? ciasteczko musimy doda?? do odpowiedzi, musimy utworzy?? j?? wcze??niej.
#     response.set_cookie(cookie_name, cookie_value, max_age=int(cookie_time) * 60) ??? dodajemy ciastko, czas musimy zrzutowa?? na int i pomno??y?? przez 60 (mamy podany czas w minutach, a ustawiamy go w sekundach). Nie przejmujemy si?? walidacj??, bo zrobimy to odpowiednim wyra??eniem regularnym w adresie URL.
#
# Usuwanie ciasteczka
#
# Na koniec musimy doda?? widok, kt??ry usunie nam ciasteczko. Poniewa?? chcemy je wy??wietli??, powinni??my je pobra??, przed usuni??ciem.
# Przyk??ad:
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
#         response = HttpResponse(f"Ciasteczko {cookie_name}:{cookie} zosta??o usuni??te")
#
#         response.delete_cookie(cookie_name)
#
#         return response
#
#     cookie = request.COOKIES.get(cookie_name) ??? pobieramy warto???? ciasteczka, korzystaj??c z metody get. Je??li ciasteczko o podanej nazwie, nie jest zapisane, dostaniemy None.
#     if not cookie: ??? je??li nie ma ciasteczka, wy??wietlamy odpowiedni komunikat.
#     response = HttpResponse(f"Ciasteczko {cookie_name}:{cookie} zosta??o usuni??te") ??? ciasteczko usuwamy z odpowiedzi, dlatego musimy utworzy?? j?? wcze??niej.
#     response.delete_cookie(cookie_name) ??? do usuni??cia ciasteczka u??ywamy metody delete_cookie.
#     return response ??? zwracamy odpowied??.
#
# Adresy URL
#
# Teraz, musimy doda?? nasze widoki do pliku urls.py, przyporz??dkowuj??c im odpowiednie adresy URL. Aby dokona?? walidacji, wykorzystamy metod?? re_path, oraz wyra??enia regularne.
# Przyk??ad:
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
#     re_path(r'^set_username/(?P<user_name>[a-zA-Z0-9]+)/$', SetUsernameView.as_view()), ??? nazwa mo??e sk??ada?? si?? tylko z liter i cyfr: [a-zA-Z0-9]+, przypisujemy j?? do zmiennej user_name.
#     path('say_hello/<int:n>/', SayHelloView.as_view()), ??? tutaj mo??emy zastosowa?? route zaznaczaj??c, ??e spodziewamy si?? typu int.
#     path('say_hello/', SayHelloView.as_view()), ??? poniewa?? parametr ustawili??my jako opcjonalny, z domy??ln?? warto??ci?? 10, mo??emy wykorzysta?? ten sam widok w dw??ch miejscach.
#     re_path(r'^create_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/(?P<cookie_value>[a-zA-Z0-9]+)/(?P<cookie_time>\d+)/$', ??? nazwa i warto???? ciasteczka powinny sk??ada?? si?? z liter i cyfr: [a-zA-Z0-9]+, czas ??ycia ciasteczka to liczba: \d+.
#     re_path(r'^delete_cookie/(?P<cookie_name>[a-zA-Z0-9]+)/$', DeleteCookieView.as_view()), ??? nazwa ciasteczka ma te same ograniczenia, co w poprzednim widoku.




lecture_details.html


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Lecture Details</title>
</head>
<body>
<h1>Nazwa wyk??adu: {{ lecture.name }}</h1>
<h2>Wyk??adowca: {{ lecture.lecturer }}</h2>
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
// Nie u??ywajcie eventu DOMContentLoaded. Skrypt jest wczytany do pliku html przed ko??cem body.
// Napiszcie funkcj?? o nazwie concatArray(array1, array2), kt??ra przyjmuje jako parametry dwie tablice.
// Niech funkcja ta zwraca now?? tablic?? b??d??c?? po????czeniem tych dw??ch.


function concatArray(array1, array2){
   return array1.concat(array2) 
}


concatArray( [1,3],[3,5] );
console.log(concatArray( [1,3],[3,5] ));
 

 








// Zadanie 2

// U??ywaj??c JavaScript dopiszcie do wszystkich div??w o klasie color nas??uchiwanie zdarze??, 
// kt??re po najechaniu na element sprawi, ??e kolor diva zmieni si?? na losowy, a na divie poka??e si?? 
// tekst trzymany w data-text.
// Zjechanie z diva powinno usuwa?? tekst, ale div powinien zosta?? pokolorowany.
// Ponowne najechanie powinno zmieni?? kolor t??a i znowu wy??wietli?? tekst.
// Hint: ??eby uzyska?? losowy kolor u??yj poni??szego kodu:
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

// W tym zadaniu mo??ecie u??ywa?? eventu DOMContentLoaded.
// Do wszystkich guzik??w znajduj??cych si?? na stronie dopiszcie event tak,
// aby po naci??ni??ciu przycisku w divie o id container pojawi?? si?? tekst trzymany w data-text.








<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h3> Tekst z atrybutu dataset z guzik??w powinien pojawia?? si?? w tym kontenerze </h3>

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

// W tym zadaniu mo??ecie u??ywa?? eventu DOMContentLoaded.

// Na stronie znajduje si?? lista zakup??w.
// Popatrzcie na HTML i zobaczcie jak lista jest zbudowana.
// Dopiszcie odpowiedni?? obs??ug?? event??w tak, aby:

//     po klikni??ciu przycisku pierwszego do listy zosta?? dopisany nowy produkt - chleb.
//     po klikni??ciu przycisku drugiego z listy by?? usuwany ostatni element.
//     po klikni??ciu przycisku trzeciego na ko??cu listy by?? dodawany nowy produkt, kt??ry jest klonem drugiego produktu - o ile ten istnieje.




<!DOCTYPE html>
<html lang="pl-PL">
<head>
    <meta charset="UTF-8">
    <title>Zadanie 4</title>
 
    <script type="text/JavaScript" src="app.js"></script>
</head>
<body>

<h1>Lista zakup??w</h1>

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
        M??ka
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
 

Wasz sklep internetowy zajmuje si?? sprzeda???? ksi????ek.
Wprowadzacie nowy produkt do oferty czyli ebooki.

Stworzenie klasy bazowej Stw??rzcie klas?? o nazwie Product.
B??dzie to klasa, kt??ra w swoim konstruktorze powinna ustawia?? takie dane jak

    title - tytu?? produktu ,
    author - autor

Stworzenie obiekt??w
W zwi??zku z dodaniem do oferty nowego produktu - ebooka - stw??rzcie dwie klasy dziedzicz??ce po klasie bazowej:
-Ebook, -Book.

Utw??rzcie te klasy w taki spos??b, aby mo??na by??o na ich podstawie stworzy?? nast??puj??ce obiekty:

    ebook pod tytu??em Ciemniejsze niebo napisany przez Ruben Eliassen.
    ksi????k?? pod tytu??em Najd??u??sza noc napisan?? przez Macieja Dancewicza.

Wy??wietlanie informacji o produkcje

    W odpowiedniej klasie stw??rzcie metod?? printInfo().
    Do wy??wietlanie wykorzystajcie ten szablon tekstu:
    ${this.constructor.name} - title: ${this.title}, author: ${this.author}

Zamawianie produkt??w
Wasi klienci chc?? m??c ??ci??ga?? oraz zamawia?? ksi????ki na podany adres.
Stw??rzcie w odpowiednich klasach nast??puj??ce metody:

    download - kt??ra wypisuje w konsoli tekst ??ci??ganie... [tutaj wstawcie tytu??]. Niech ten tekst r??wnie?? b??dzie zwracany przez metod?? opr??cz wypisania w konsoli.
    order - kt??ra wypisuje w konsoli tekst Podaj adres dostawy! Niech ten tekst r??wnie?? b??dzie zwracany przez metod?? opr??cz wypisania w konsoli.








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
    const text = '??ci??ganie... ' + this.title;
    console.log(text);
    return text;
  }
}


const book = new Book('Najd??u??sza noc', 'Maciej Dancewicz');
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

// Korzystaj??c z adresu https://swapi.dev/api/starships wczytajcie na stron?? informacje o statkach z Gwiezdnych Wojen.
// Kolejne statki wstawcie do listy.
// Nazwy statk??w wczytajcie do element??w h2, natomiast model do element??w h3.
// Utw??rzcie te elementy i wstawcie je do DOM.
// Zauwa??cie, ??e dane nas interesuj??ce znajduj?? si?? w tablicy, kt??ra znajduje si?? w jednym ze zwracanych w obiekcie atrybut??w.

// Hint:
// Zobaczcie jak wygl??da w konsoli obiekt, kt??ry otrzymujecie jako odpowied??, zanim wstawicie content na stron??.


getData('https://swapi.dev/api/starships');


function getData(url) {

    fetch(url)
        .then(response => {
            return response.json();
        })
        .then(data => {
            


 
            const tasks = data.results;
            console.log('Odpowied?? z serwera to:', data);
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





