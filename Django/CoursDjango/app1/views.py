from django.shortcuts import render
from django.db.models import F
from .models import Question


def index(request):
    return render(request, 'app1/index.html')
# Create your views here.
