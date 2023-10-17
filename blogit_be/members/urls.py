from django.urls import path, re_path, include
from .views import UserRegiterView,PasswordsChangeView,UserEditView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
   path('register/',UserRegiterView.as_view(),name = 'register'),
   path('edit_profile/',UserEditView.as_view(),name = 'edit_profile'),
   path('password/',PasswordsChangeView.as_view(template_name = 'registration/change-password.html'),name = 'password_change'),
   path('password-success/',views.password_success,name = 'password_success')
]   
