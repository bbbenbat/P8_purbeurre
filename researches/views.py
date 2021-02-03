from django.shortcuts import render

from researches.api import best_product
from researches.models import Product, Favorite


def main_page(request):
    return render(request, 'index.html')


def favorite_product(request):
    current_user = request.user
    favorites = Favorite.objects.filter(id_user=1)
    list_prod = []
    for req in favorites:
        prod = Product.objects.filter(pk=req.id_product_id)
        for req1 in prod:
            list_prod.append({'product': req1.name, 'date': str(req.date)})
    return render(request, 'favorite_product.html', {'favorites': list_prod})


def product_research(request):
    list_product_category = []
    request_user = request.POST.get('question').lower()
    if request_user == '':
        list_product = None
        return render(request, 'research_product.html', {'product': list_product, 'test_prod': request_user})
    else:
        best_prod = best_product.BestResearch()
        list_product = best_prod.bestresearch_all(request_user)[:6]
        # list_category = Category.objects.filter(name__contains=request_user)
        return render(request, 'research_product.html', {'product': list_product, 'test_prod': request_user})
