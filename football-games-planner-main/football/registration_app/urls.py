from django.urls import path

from .views import UserReqgisterView

urlpatterns = [
    path('register/', UserReqgisterView.as_view(), name='register'),
]
