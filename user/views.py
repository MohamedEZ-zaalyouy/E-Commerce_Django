from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Category
from user.models import UserProfile
# Create your views here.

# ============================================
#     Create index views here.
# ============================================


def index(request):
    return HttpResponse(" Hi user")


# ============================================
#     Create login views here.
# ============================================


def login_form(request):
    category = Category.objects.all()
    if request.method == 'POST':  # check post
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(
                request, "Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/login')
    # Return an 'invalid login' error message.

    context = {
        'category': category,
    }
    return render(request, 'login.html', context)

# ============================================
#     Create logout_func  here.
# ============================================


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')


# ============================================
#     Create signup views here.
# ============================================


def signup(request):
    category = Category.objects.all()
    context = {
        'category': category,
    }
    return render(request, 'signup.html', context)
