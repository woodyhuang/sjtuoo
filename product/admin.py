from django.contrib import admin

from product.models import ProductCategory, Product

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price','created_time')

admin.site.register(Product, ProductAdmin)
