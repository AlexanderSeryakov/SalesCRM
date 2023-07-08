from rest_framework.response import Response
from apps.product.models import Product


def add_product_quantity(products):
    try:
        for product in products:
            current_product = Product.objects.get(pk=int(product['productId']))
            current_product.in_stock += int(product['quantity'])
            current_product.save()
    except KeyError:
        return Response({'Incorrect data': 400})
    except Exception:
        return Response({'Unknown Error': 400})
    
    return True