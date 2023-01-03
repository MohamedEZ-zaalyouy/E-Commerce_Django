from django.shortcuts import render
from django.http import HttpResponse
from home.models import Setting


# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting
    }
    return render(request, 'index.html', context)


def aboutus(request):
    return HttpResponse("aboutus")


def contact(request):
    return HttpResponse("contact")
