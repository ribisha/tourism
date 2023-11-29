from django.shortcuts import render
from .models import *

def index(request):
    place=places.objects.all()
    tm=teams.objects.all()
    return render(request,'index.html', {'location':place, 'team':tm})
