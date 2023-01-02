from django.contrib import admin
from .models import Category, Product, Images


# ===========================
# setting your admin models.
# ===========================
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title', 'status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['category']
   # readonly_fields = ('image_tag',)
   # inlines = [ProductImageInline,ProductVariantsInline,ProductLangInline]
    prepopulated_fields = {'slug': ('title',)}


# ===========================
# Register your models here.
# ===========================
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
