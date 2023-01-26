from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from home.models import Setting, ContactForm, ContactMessage
from product.models import Category, Product


# Create your views here.

# ========================================================
# Create index Views
# ========================================================

def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('-id')[:4]
    page = 'home'
    context = {
        'setting': setting,
        'page': page,
        'category': category,
        'product_slider': product_slider,

    }
    return render(request, 'index.html', context)

# ========================================================
# Create About Us Views
# ========================================================


def aboutus(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting
    }
    return render(request, 'aboutus.html', context)


# ========================================================
# Create Contact Views
# ========================================================


def contact(request):
    # category = categoryTree(0,'',currentlang)
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(
                request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {
        'setting': setting,
        'form': form,
    }
    return render(request, 'contact.html', context)

# ========================================================
# Create category_products Views
# ========================================================


def category_products(request, id, slug):
    products = Product.objects.filter(category_id=id)
    return HttpResponse(products)
