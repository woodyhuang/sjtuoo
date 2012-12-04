from product.models import ProductCategory
from order.forms import ShoppingCartForm

def extra_params(request):
    return {
            'categories': ProductCategory.objects.all(),
            'shop_cart': ShoppingCartForm(request)
            }