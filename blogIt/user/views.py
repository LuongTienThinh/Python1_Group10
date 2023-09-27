from django.shortcuts import render
# from user.models import 

# Create your views here.

def index(request):
    return render(request, 'index.html')