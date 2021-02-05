from django.shortcuts import render

from researches.controllers import best_product, favorites


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
    url_product = request.POST.get('urlprod')
    return render(request, 'info_product.html', {'url_product': url_product})


def legal(request):
    return render(request, 'legal.html')
