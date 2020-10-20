from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
# ==================================================
# When there is a request to:
# http://127.0.0.1:8000/products,
# this view function(index) will be called.
# That is: mapping this URL:
# http://127.0.0.1:8000/products, to index function
# ==================================================
def index(request):
    products = Product.objects.all()
    return render(
        request,
        'index.html',
        {
            'products': products
        }
    )


def get_new_products(request):
    return HttpResponse('This are the list of new products')

