# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'staffs/index.html')

def hours(request):
    return render(request, 'staffs/hours.html')