from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404

def home(request):
     title='Home | MyGram'
     return render(request,'grams/home.html',{'title':title})
    

# Create your views here.
