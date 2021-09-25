from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('football_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration_app.urls')),
]
