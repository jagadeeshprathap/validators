from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def student(request):
    SFO=studentform()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=studentform(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
    return render(request,'student.html',d)