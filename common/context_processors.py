from product.models import ProductCategory

def extra_params(request):
    return {
            'categories': ProductCategory.objects.all(),
            }