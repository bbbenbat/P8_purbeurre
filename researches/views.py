from django.shortcuts import render

from researches.controllers import best_product, favorites
from researches.models import Product, Favorite


def main_page(request):
    return render(request, 'index.html')


def favorite_product(request):
    current_user = request.user
    favproduct = favorites.Favorites()
    list_prod = favproduct.show_favorite(current_user.id)
    return render(request, 'favorite_product.html', {'favorites': list_prod})

def favorite_save(request):
    request_user = request.POST.get('favprod')
    current_user = request.user
    favproduct = favorites.Favorites()
    favproduct.save_favorite(request_user, current_user.id)
    list_prod = favproduct.show_favorite(current_user.id)
    return render(request, 'favorite_product.html', {'favorites': list_prod, 'request_user': request_user})




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
