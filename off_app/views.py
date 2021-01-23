from django.shortcuts import render

from off_app.models import Product


def main_page(request):
    return render(request, 'index.html')


def product_research(request):
    product_user = request.POST.get('question')
    list_product = Product.objects.filter(name__contains=product_user)
    return render(request, 'research_product.html', {'product': list_product})



