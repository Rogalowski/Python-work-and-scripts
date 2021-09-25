DJANGO ZAAWANSOWANE DZIEN 1 ANNOTATE AVARAGE DISTINCT JINJA SZABLONY PROCESOR KONTEKTU DJANGO ZAAWANSOWANE DZIEN 1 ANNOTATE AVARAGE DISTINCT JINJA SZABLONY PROCESOR KONTEKTU 
DJANGO ZAAWANSOWANE DZIEN 1 ANNOTATE AVARAGE DISTINCT JINJA SZABLONY PROCESOR KONTEKTU 
DJANGO ZAAWANSOWANE DZIEN 1 ANNOTATE AVARAGE DISTINCT JINJA SZABLONY PROCESOR KONTEKTU DJANGO ZAAWANSOWANE DZIEN 1 ANNOTATE AVARAGE DISTINCT JINJA SZABLONY PROCESOR KONTEKTU 
views.python


from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades
from django.db.models import Avg

class SchoolView(View):
    def get(self, request):
        #zakomentowane bo towrzymy extends, dzeidziczenie po html
        # html = """<!doctype html>
        # <html>
        #     <head><meta charset="utf-8"></head>
        #     <body>
        #         <h1>Szkoła podstawowa nr 1 im. Chucka Norrisa.</h1>
        #         <h2>Klasy:</h2>
        #         <ul>
        #             {}
        #         </ul>
        #     </body>
        # </html>
        # """
        # class_list = []
        # for school_class in SCHOOL_CLASS:
        #     class_list.append("<li><a href='/class/{}'>{}</a></li>".format(school_class[0], school_class[1]))
        # classes_part = "".join(class_list)
        return render(request, 'exercises_app/school_class_list.html',
               context={
                   'school_classes': SCHOOL_CLASS,
               }
               )
        # return HttpResponse(html.format(classes_part)) odczytuje html wyrzej , komentujemy zeby uzyc bazowego html dzidziczacego extends


# Zadanie 3
# Zapoznaj się z widokiem SchoolClassView. Sprawdź w pliku urls.py, w jaki sposób ten widok jest udostępniany w aplikacji.
# Napisz szablon, który zaprezentuje listę uczniów w pokazywanej klasie.
#
# Podpowiedź: do renderowania danych kontekstowych użyj komend szablonów {% for ... in ... %} ... {% endfor %} i {% if ... %} ... {% endif %}

class SchoolClassView(View):
    def get(self, request, school_class):
        students = Student.objects.filter(school_class=school_class)
        return render(request, "exercises_app/class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(school_class-1)][-1]})


# class StudentsView(View):
#     def get(self, request, student_id):
#         subjects = SchoolSubject.objects.all() #get(id=student_id)
#         student = Student.objects.get(id=student_id)
#         return render(request, "exercises_app/student_details.html", {"student": student, 'subjects': subjects})
# #https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.get_FOO_display



class StudentsView(View):
    def get(self, request, student_id):
        # subjects = StudentGrades.objects.filter(
        # student__pk=student_id).distinct('school_subject')
        # .values_list('school_subject__name')
        subjects = StudentGrades.objects.filter(
            student__pk=student_id).distinct('school_subject') #odwolanie do tabeli school_subject jeden do wielu
        return render(
            request,
            'exercises_app/student_details.html',
            context={
                'student': Student.objects.get(pk=student_id),
                'subjects': subjects,
            },
        )


class GradesView(View):
    def get(self, request, student_id, subject_id):

        subjects = SchoolSubject.objects.get(id=subject_id)  # get(id=student_id)
        student = Student.objects.get(id=student_id)
        grades = StudentGrades.objects.filter(student_id=student_id, school_subject_id=subject_id)

        def srednia():
            suma = 0
            for grade in grades:
                suma += grade.grade
            return suma / len(grades)

        return render(request, "exercises_app/student_grades.html", {"student": student, 'subjects': subjects, 'grades': grades, 'srednia': srednia()})

# Rwiązanie Dawida, utworzenie wirtualnej tabeli ktora sumuje wartosci, zamiast przechodzic po wsyzstkich wartosciach, za pomoca avarage
    # class StudentGradesDetailView(View):
    #     def get(self, request, *args, **kwargs):
    #         student = Student.objects.get(pk=kwargs['student_id'])
    #         subject = SchoolSubject.objects.annotate(
    #             average_grade=Avg('studentgrades__grade')
    #         ).get(pk=kwargs['subject_id'])
    #         breakpoint()
    #         context = {
    #             'student': student,
    #             'subject': subject,
    #         }
    #         return render(request, 'exercises_app/student_grades_detail.html', context)

#     { % extends 'base.html' %}
#     { % block
#     content %}
#     < h2 > {{student.last_name}} | {{student.get_school_class_display}} < / h2 >
#     < h3 > {{subject.name}}
#     {{subject.teacher_name}} < / h3 >
#     < ul >
#     < h4 > Grades: < / h4 >
#     { %
#     for student_grade in student.studentgrades_set.all %}
#     < li > {{student_grade.grade}} < / ul >
#
#
# { % endfor %}
# < / ul >
# < h4 > Average: < / h4 >
# {{subject.average_grade}}
# { % endblock %}




#     { % extends 'base.html' %}
#     { % block
#     content %}
#     < h2 > {{student.last_name}} | {{student.get_school_class_display}} < / h2 >
#     < h3 > {{subject.name}}
#     {{subject.teacher_name}} < / h3 >
#     < ul >
#     < h4 > Grades: < / h4 >
#     { %
#     for student_grade in student.studentgrades_set.all %}
#     < li > {{student_grade.grade}} < / ul >
#
#
# { % endfor %}
# < / ul >
# < h4 > Average: < / h4 >
# {{subject.average_grade}}
# { % endblock %}

base.html_name
<!DOCTYPE html>
<html lang="en">
<html>
            <head><meta charset="utf-8"></head>
            <body>
            {% block content %}
                <h1>Szkoła podstawowa nr 1 im. Chucka Norrisa.</h1>
                <h2>Klasy:</h2>
                <ul>
                    <li><a href='/class/{}'>{}</a></li>
                </ul>
            {% endblock content %}
            </body>
        </html>


        {% extends 'base.html' %}


student_detail.html

{#{% extends 'base.html' %}#}
{##}
{##}
{##}
{#{% block content %}#}
{#<h1>Szkoła podstawowa nr 1 im. Chucka Norrisa.</h1>#}
{#                <h2>Klasa: {{ student.get_school_class_display }}</h2>#}
{#    https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.get_FOO_display get_school_class_display#}
{##}
{#               <h4>{{ student.name }}</h4>#}
{#                {% for subject in subjects %}#}
{##}
{##}
{##}
{#                 <ul>#}
{#                    <li><a href='/grades/{{ student.id }}/{{ subject.id }}'>{{ subject.name }}</a></li>#}
{#                     LUB#}
{#<a href="grades/{{student.pk}}/{{subject.school_subject.pk}}">{{subject.school_subject.name}}</a>#}
{#                </ul>#}
{##}
{#    {% endfor %}#}
{#{% endblock %}#}



{% extends "base.html" %}

{% block content %}
<h4>Name: {{ student.first_name }}</h4>
<h4>Surname: {{ student.last_name}}</h4>
<h3>Class: {{ student.get_school_class_display }}</h3>

Subjects:
{% for subject in subjects %}
    <br>
<a href="grades/{{student.pk}}/{{subject.school_subject.pk}}">{{subject.school_subject.name}}</a>
{% endfor %}

{% endblock content %}




student_grades.html details

{% extends 'base.html' %}



{% block content %}
<h1>Szkoła podstawowa nr 1 im. Chucka Norrisa.</h1>
                <h2>Klasa: {{ student.get_school_class_display }}</h2>
    https://docs.djangoproject.com/en/3.2/ref/models/instances/#django.db.models.Model.get_FOO_display get_school_class_display

    Student :     <h4>{{ student.name }}</h4>

    Subject : {{ subjects.name }} <br>
   <p>Teacher: {{ subjects.teacher_name }}  </p>
    <p>Oceny:</p>

{% for grade in grades %}
{{ grade.grade }} = {{grade.get_grade_display }},
    {% endfor %}

    <br>
Średnia ocen: {{ srednia }}
                 <ul>


                </ul>


{% endblock %}

{## Rwiązanie Dawida, utworzenie wirtualnej tabeli ktora sumuje wartosci, zamiast przechodzic po wsyzstkich wartosciach, za pomoca avarage#}
{#{% extends 'base.html' %}#}
{#{% block content %}#}
{#    <h2> {{ student.last_name }} | {{ student.get_school_class_display }}</h2>#}
{#    <h3> {{ subject.name }} {{ subject.teacher_name }} </h3>#}
{#    <ul>#}
{#        <h4> Grades: </h4>#}
{#        {% for student_grade in student.studentgrades_set.all %}#}
{#            <li>{{ student_grade.grade }}</ul>#}
{#        {% endfor %}#}
{#    </ul>#}
{#    <h4>Average:</h4>#}
{#    {{ subject.average_grade }}#}
{#{% endblock %}#}








setting.py 
"""
Django settings for coderslab project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a*!!w1bzt3+^ne4a-y91vi!_b&hkd3dk&%u8@@$0fx(0lr1pfo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exercises_app',
    'homework_app',
    #LUB
    # 'homework_app.apps.HomeworkAppConfig',
    # 'exercises_app.apps.ExercisesAppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # 'coderslab.my_context_processor.my_cp',
]

ROOT_URLCONF = 'coderslab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Funckja globalna kontekstóœ widocznych we wszystkich templatkach
# from datetime import datetime
# def my_cp(request):
#   ctx = {
#     "now": datetime.now(),
#     "version": "1.0",
#   }
#   return ctx


WSGI_APPLICATION = 'coderslab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'HOST': '127.0.0.1',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'python_module5',
        'USER': 'postgres',
        'PASSWORD': 'coderslab',
        'PORT': 5431,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'