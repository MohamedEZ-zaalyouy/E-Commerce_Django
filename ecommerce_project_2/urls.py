"""ecommerce_project_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views
from order import views as OrderViews

urlpatterns = [
    path('', include("home.urls")),
    path('admin/', admin.site.urls),
    path('home/', include("home.urls")),
    path('product/', include("product.urls")),
    path('order/', include("order.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path('category/<int:id>/<slug:slug>',
         views.category_products, name='category_products'),
    path('search/', views.search, name='search'),
    path('shopcart/', OrderViews.shopcart, name='shopcart'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('product/<int:id>/<slug:slug>',
         views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
