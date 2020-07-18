from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def dateinfo(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Friend</h1>'
    msg=msg+'<h1>Now the time is '+str(date)+'</h1>'
    return HttpResponse(msg)
