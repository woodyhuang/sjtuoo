from django.contrib import admin

from product.models import ProductCategory

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(ProductCategory, ProductCategoryAdmin)
