#from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'static_handler.html')
#    return HttpResponse(u'Привет, мир')

