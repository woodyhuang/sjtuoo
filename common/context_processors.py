from product.models import ProductCategory
from order.forms import ShoppingCardForm

def extra_params(request):
    return {
            'categories': ProductCategory.objects.all(),
            'shop_cart': ShoppingCardForm(request)
            }