from django.contrib import admin

from product.models import ProductCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','imgurl')

admin.site.register(Product, ProductAdmin)
