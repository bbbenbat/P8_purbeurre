from django.shortcuts import render

from researches.models import Product, Category, ProductCategory
from researches.api import best_product


def main_page(request):
    return render(request, 'index.html')


def product_research(request):
    list_product_category = []
    request_user = request.POST.get('question').lower()
    if request_user == '':
        list_product = None
        return render(request, 'research_product.html', {'product': list_product, 'test_prod': request_user})
    else:
        best_prod = best_product.BestResearch()
        list_product = best_prod.bestresearch_all(request_user)[:6]
        #list_category = Category.objects.filter(name__contains=request_user)
        return render(request, 'research_product.html', {'product': list_product, 'test_prod': request_user})



