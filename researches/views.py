from django.shortcuts import render
from django.views.generic import TemplateView

from researches.controllers import best_product, favorites, info_prod

favproduct = favorites.Favorites()


class HomePageView(TemplateView):
    template_name = 'home.html'


def favorite_product(request):
    """ Give the favorite products to the page favorite_product.html . """

    current_user = request.user
    favproduct = favorites.Favorites()
    list_prod = favproduct.show_favorite(current_user.id)
    return render(request, 'favorite_product.html', {'favorites': list_prod})


def favorite_save(request):
    """ Save as favorite the product selected by the user. """
    id_product = request.POST.get('favprod')
    current_user = request.user
    favproduct.save_favorite(id_product, current_user.id)
    list_prod = favproduct.show_favorite(current_user.id)
    return render(request, 'favorite_product.html',
                  {'favorites': list_prod, 'request_user': id_product})


def favorite_update(request):
    """ Update the product favorite statut. """

    current_user = request.user
    update_user = request.POST.get('favorite_statut')
    id_product = request.POST.get('id_product')
    favproduct.update_favorite(update_user, current_user, id_product)
    return favorite_product(request)


def product_research(request):
    """ Return a list of product according to the written product. """

    request_user = request.POST.get('question').lower()
    if request_user == '':
        return render(request, 'home.html')
    else:
        try:
            best_prod = best_product.BestResearch()
            list_product = best_prod.bestresearch_all(request_user)[:6]
            if request.user:
                current_user = request.user
            else:
                current_user = None
            list_prod = favproduct.statut_fav_from_prod(list_product,
                                                        current_user.id)[:6]
            return render(request, 'research_product.html',
                          {'product': list_prod, 'test_prod': request_user})
        except:
            list_product = None
            return render(request, 'research_product.html',
                          {'product': list_product,
                           'test_prod': request_user})


def info_product(request):
    """ Return the information about the selected product. """

    prod_id = request.POST.get('prod_id')
    infoprod = info_prod.InfoProd()
    list_all = infoprod.find_product(prod_id)
    list_prod = list_all[0]
    list_p = list_all[1]
    fat = list_prod['fat_100g']
    saturated = list_prod['saturated-fat_100g']
    sugar = list_prod['sugars_value']
    salt = list_prod['salt_100g']
    energy = list_prod['energy_100g']
    list_nutri = ['a', 'b', 'c', 'd', 'e']
    return render(request, 'info_product.html',
                  {'prod_id': prod_id, 'list_nutri': list_nutri,
                   'fat': fat, 'saturated': saturated,
                   'salt': salt, 'sugar': sugar, 'energy': energy,
                   'nutriscore': list_p['nutriscore'],
                   'url_image': list_p['url_image'],
                   'name': list_p['name'], 'url': list_p['url'],
                   'barcode': list_p['barcode'],
                   'ingredient': list_p['ingredient']})


def legal(request):
    """ Return the legal page. """

    return render(request, 'legal/legal.html')


def profil_user(request):
    """ Return the account page. """

    return render(request, 'account/profil_user.html')
