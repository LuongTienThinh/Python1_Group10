from django.urls import path, re_path, include
from .views import UserRegiterView

urlpatterns = [
   path('register/',UserRegiterView.as_view(),name = 'register')
]   
