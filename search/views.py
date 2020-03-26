from django.shortcuts import render
from products.models import Product


# Create your views here.
def do_search(request):
    products = Product.objects.filter(name_icontains=request.request.GET['q'])
    return render(request, 'product.html', {'products': products})