from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .form import SignUpForm,ChangePasswordForm,EditProfileForm
# Create your views here.
class UserRegiterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user    

  
class PasswordsChangeView (PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'registration/password_success.html')