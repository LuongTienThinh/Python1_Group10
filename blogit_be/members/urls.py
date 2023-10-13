from django.urls import path, re_path, include
from .views import UserRegiterView,PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   path('register/',UserRegiterView.as_view(),name = 'register'),
   path('password/',PasswordsChangeView.as_view(template_name = 'registration/change-password.html'),name = 'password_change'),
   path('password-success/',views.password_success,name = 'password_success')
]   
