from django.shortcuts import render
from .models import *
# Create your views here.

def discuss(request):
    context ={
        'questions': Question.objects.all()
    }
    return render(request,'d_forum/discuss.html',context)