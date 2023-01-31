from django.contrib import admin
from order.models import ShopCart


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']

# =================================
# Register your models order here.
# =================================


admin.site.register(ShopCart, ShopCartAdmin)
