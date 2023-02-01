from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from home.models import Setting, ContactForm, ContactMessage
from product.models import Category, Product, Images, Comment
from order.models import ShopCart
from home.forms import SearchForm
import json

# Create your views here.

# ========================================================
# Create index Views
# ========================================================


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('-id')[:4]
    product_latest = Product.objects.all().order_by(
        '-id')[:4]  # last 4 products
    product_picked = Product.objects.all().order_by(
        '?')[:4]  # Random selected 4 products
    page = 'home'
    # start shop cart min en home page
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    nbr_ord = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
        nbr_ord += 1
    # end shop cart min en home page
    context = {
        'setting': setting,
        'page': page,
        'category': category,
        'product_slider': product_slider,
        'product_latest': product_latest,
        'product_picked': product_picked,
        'shopcart': shopcart,
        'total': total,
        'nbr_ord': nbr_ord,

    }
    return render(request, 'index.html', context)

# ========================================================
# Create About Us Views
# ========================================================


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
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
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactForm
    context = {
        'setting': setting,
        'category': category,
        'form': form,
    }
    return render(request, 'contact.html', context)

# ========================================================
# Create category_products Views
# ========================================================


def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_products.html', context)

# ========================================================
# Create search Views
# ========================================================


def search(request):
    if request.method == 'POST':  # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']  # get form input data
            catid = form.cleaned_data['catid']
            if catid == 0:
                # SELECT * FROM product WHERE title LIKE '%query%'
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(
                    title__icontains=query, category_id=catid)

            category = Category.objects.all()
            context = {
                'products': products,
                'query': query,
                'category': category}

        return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')

# ========================================================
# Create search_auto Views
# ========================================================


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

# ========================================================
# Create product_detail Views
# ========================================================


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {
        'category': category,
        'product': product,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)
