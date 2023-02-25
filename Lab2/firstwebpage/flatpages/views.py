from django.http import HttpResponse


def home(request):
    return HttpResponse(u'Привет, мир')
# Create your views here.
