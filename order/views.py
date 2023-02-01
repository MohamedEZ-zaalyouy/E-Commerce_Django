from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from order.models import ShopCart, ShopCartForm
from product.models import Category

# Create your views here.

# ============================================
#     Create index views here.
# ============================================


def index(request):
    return HttpResponse(" Hi order")

# ============================================
#     Create addtoshopcart views here.
# ============================================


@login_required(login_url='/login')  # Check login
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information

    checkproduct = ShopCart.objects.filter(
        product_id=id)  # Check product in shopcart
    if checkproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  #
            else:  # Inser to Shopcart
                data = ShopCart()  # model ile bağlantı kur
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()  #
            messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)
    else:  # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()  #
        else:  # Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)

# ============================================
#     Create  views here.
# ============================================


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               }
    return render(request, 'shopcart_products.html', context)


# ============================================
#     Create deletefromcart views here.
# ============================================
@login_required(login_url='/login')  # Check login
def deletefromcart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    ShopCart.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect(url)
