from django.contrib import admin
from .models import Category, Product, Images


# ===========================
# setting your admin models.
# ===========================
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title', 'status']

# add la table Image en table Product


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}
    # ,ProductVariantsInline,ProductLangInline


# ===========================
# Register your models here.
# ===========================
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
