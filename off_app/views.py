from django.shortcuts import render

from off_app.models import Product


def research_product(request):
    products = Product.objects.all()
    return render(request, 'research_product.html', {'product':products})
