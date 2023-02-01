from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# ============================================
#     Create index views here.
# ============================================


def index(request):
    return HttpResponse(" Hi user")
