from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .form import SignUpForm,ChangePasswordForm
# Create your views here.
class UserRegiterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class PasswordsChangeView (PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html')