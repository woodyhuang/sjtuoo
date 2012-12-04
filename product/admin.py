from django.contrib import admin

from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','imgurl')

admin.site.register(Product, ProductAdmin)
