from django.urls import reverse_lazy
from django.views.generic import CreateView

from football_app.models import User
from registration_app.forms import UserRegisterForm


class UserReqgisterView(CreateView):
    """Returns the user registration form"""
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
