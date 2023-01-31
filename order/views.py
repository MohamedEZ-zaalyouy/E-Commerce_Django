from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from product.models import CommentForm, Comment

# Create your views here.


def index(request):
    return HttpResponse(" Hi order")
