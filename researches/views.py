from django.shortcuts import render
from django.views.generic import TemplateView

from researches.controllers import best_product, favorites

class HomePageView(TemplateView):
    template_name = 'home.html'

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
    request_user = request.POST.get('question').lower()
    if request_user == '':
        return render(request, 'home.html')
    else:
        try:
            best_prod = best_product.BestResearch()
            list_product = best_prod.bestresearch_all(request_user)[:6]
            return render(request, 'research_product.html', {'product': list_product, 'test_prod': request_user})
        except:
            list_product = None
            return render(request, 'research_product.html', {'product': list_product, 'test_prod': request_user})


def info_product(request):
    prod_url = request.POST.get('prod_url')
    prod_id = request.POST.get('prod_id')
    prod_name = request.POST.get('prod_name')
    return render(request, 'info_product.html',
                  {'prod_url': prod_url, 'prod_id': prod_id, 'prod_prod': prod_name})


def legal(request):
    return render(request, 'legal/legal.html')


def profil_user(request):
    return render(request, 'account/profil_user.html')
