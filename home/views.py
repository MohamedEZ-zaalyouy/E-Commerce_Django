from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from home.models import Setting, ContactForm, ContactMessage, FAQ, SettingLang, Language
from user.models import UserProfile
from product.models import Category, Product, Images, Comment, Variants, CategoryLang
from order.models import ShopCart
from home.forms import SearchForm
import json
from django.template.loader import render_to_string
from django.utils import translation
from django.contrib.auth.decorators import login_required
from ecommerce_project_2 import settings
# Create your views here.

# ========================================================
# Create index Views
# ========================================================


def index(request):

    setting = Setting.objects.get(pk=1)
    product_latest = Product.objects.all().order_by(
        '-id')[:4]  # last 4 products
    # >>>>>>>>>>>>>>>> M U L T I   L A N G U G A E >>>>>> START
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]

    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)
        product_latest = Product.objects.raw(
            'SELECT p.id,p.price, l.title, l.description,l.slug  '
            'FROM product_product as p '
            'LEFT JOIN product_productlang as l '
            'ON p.id = l.product_id '
            'WHERE  l.lang=%s ORDER BY p.id DESC LIMIT 4', [currentlang])

    setting = Setting.objects.get(pk=1)
    # category = Category.objects.all()
    product_slider = Product.objects.all().order_by('-id')[:4]
    # product_latest = Product.objects.all().order_by('-id')[:4]  # last 4 products
    product_picked = Product.objects.all().order_by(
        '?')[:4]  # Random selected 4 products
    page = 'home'

    context = {
        'setting': setting,
        'page': page,
        # 'category': category,
        'product_slider': product_slider,
        'product_latest': product_latest,
        'product_picked': product_picked,
    }
    return render(request, 'index.html', context)

# ========================================================
# Create About Us Views
# ========================================================


def aboutus(request):
    # category = categoryTree(0,'',currentlang)
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

    context = {'setting': setting}
    return render(request, 'aboutus.html', context)


# ========================================================
# Create Contact Views
# ========================================================


def contact(request):
    currentlang = request.LANGUAGE_CODE[0:2]
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

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

    form = ContactForm
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)

# ========================================================
# Create category_products Views
# ========================================================


def category_products(request, id, slug):
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)  # default language
    if defaultlang != currentlang:
        try:
            products = Product.objects.raw(
                'SELECT p.id,p.price,p.amount,p.image,p.variant,l.title, l.keywords, l.description,l.slug,l.detail '
                'FROM product_product as p '
                'LEFT JOIN product_productlang as l '
                'ON p.id = l.product_id '
                'WHERE p.category_id=%s and l.lang=%s', [id, currentlang])
        except:
            pass
        catdata = CategoryLang.objects.get(category_id=id, lang=currentlang)

    context = {'products': products,
               # 'category':category,
               'catdata': catdata}
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
    query = request.GET.get('q')
    # >>>>>>>>>>>>>>>> M U L T I   L A N G U G A E >>>>>> START
    defaultlang = settings.LANGUAGE_CODE[0:2]  # en-EN
    currentlang = request.LANGUAGE_CODE[0:2]
    # category = categoryTree(0, '', currentlang)
    category = Category.objects.all()

    product = Product.objects.get(pk=id)

    if defaultlang != currentlang:
        try:
            prolang = Product.objects.raw('SELECT p.id,p.price,p.amount,p.image,p.variant,l.title, l.keywords, l.description,l.slug,l.detail '
                                          'FROM product_product as p '
                                          'INNER JOIN product_productlang as l '
                                          'ON p.id = l.product_id '
                                          'WHERE p.id=%s and l.lang=%s', [id, currentlang])
            product = prolang[0]
        except:
            pass
    # <<<<<<<<<< M U L T I   L A N G U G A E <<<<<<<<<<<<<<< end
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
    if product.variant != "None":  # Product have variants
        if request.method == 'POST':  # if we select color
            variant_id = request.POST.get('variantid')
            # selected product by click color radio
            variant = Variants.objects.get(id=variant_id)
            colors = Variants.objects.filter(
                product_id=id, size_id=variant.size_id)
            sizes = Variants.objects.raw(
                'SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
            query = ''
            query += variant.title+' Size:' + \
                str(variant.size) + ' Color:' + str(variant.color)
            context.update({'query': query, })
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(
                product_id=id, size_id=variants[0].size_id)
            sizes = Variants.objects.raw(
                'SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
            variant = Variants.objects.get(id=variants[0].id)

        context.update({
            # 'query': query,
            'sizes': sizes,
            'colors': colors,
            'variant': variant,
        })

    return render(request, 'product_detail.html', context)


def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string(
            'color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)


# ========================================================
# Create FAQ Views
# ========================================================


def faq(request):
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]

    if defaultlang == currentlang:
        faq = FAQ.objects.filter(
            status="True", lang=defaultlang).order_by("ordernumber")
    else:
        faq = FAQ.objects.filter(
            status="True", lang=currentlang).order_by("ordernumber")

    context = {
        'faq': faq,
    }
    return render(request, 'faq.html', context)


# ========================================================
# Create selectlanguage Views
# ========================================================


def selectlanguage(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        return HttpResponseRedirect("/"+lang)

# ========================================================
# Create savelangcur Views
# ========================================================


@login_required(login_url='/login')  # Check login
def savelangcur(request):
    lasturl = request.META.get('HTTP_REFERER')
    curren_user = request.user
    language = Language.objects.get(code=request.LANGUAGE_CODE[0:2])
    # Save to User profile database
    data = UserProfile.objects.get(user_id=curren_user.id)
    data.language_id = language.id
    data.currency_id = request.session['currency']
    data.save()  # save data
    return HttpResponseRedirect(lasturl)

# ========================================================
# Create selectcurrency Views
# ========================================================


def selectcurrency(request):
    pass
