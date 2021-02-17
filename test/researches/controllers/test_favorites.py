""" This module test the class Favorites from best_product file. """

from researches.controllers import favorites
from researches.models import Favorite, Product

favo = favorites.Favorites()

ID_PRODUCT = 655
ID_USER = 1


def test_show_favorite():
    """ This method allows to find the user's favorite products.
    The user with ID '1'."""
    req = favo.show_favorite(ID_USER)
    req = req[0]
    fav = Favorite.objects.filter(id_user_id=ID_USER).order_by('date')
    for loop in fav:
        result = loop.id_product_id
    assert req['id'] == result


def test_save_favorite():
    """ This method allows to save the user's favorite products.
    The 'id_product' number has not be safe in Favorite table with the user id."""

    favo.save_favorite(ID_PRODUCT, ID_USER)
    req = Favorite.objects.get(id_product_id=ID_PRODUCT, id_user_id=ID_USER)
    assert req


def test_update_favorite():
    """ Update favorite product statut of the user (active or not). """
    statut = False
    favo.update_favorite(statut, ID_USER, ID_PRODUCT)
    fav = Favorite.objects.filter(id_user_id=ID_USER, id_product_id=ID_PRODUCT).order_by('date')
    for loop in fav:
        req = loop.active
    result = False
    assert req == result


def test_statut_fav_from_prod():
    """ Give the list of product with favorite statement. """
    fav = Favorite.objects.filter(id_user_id=ID_USER).values_list('id_product_id', flat=True)
    prod = Product.objects.filter(pk__in=fav)
    req = favo.statut_fav_from_prod(prod, ID_USER)
    result = [{'active': True, 'id_user': 1, 'id_product_fav': 600, 'nutriscore': 'd', 'id_product': 600,
               'url_image': 'https://static.openfoodfacts.org/images/products/307/378/107/0279/front_fr.111.400.jpg',
               'name': 'la vache qui rit'},
              {'active': False, 'id_user': 1, 'id_product_fav': 733, 'nutriscore': 'd', 'id_product': 733,
               'url_image': 'https://static.openfoodfacts.org/images/products/312/448/000/2501/front_fr.149.400.jpg',
               'name': 'schweppes agrumes'},
              {'active': False, 'id_user': 1, 'id_product_fav': 510, 'nutriscore': 'b', 'id_product': 510,
               'url_image': 'https://static.openfoodfacts.org/images/products/500/011/261/1762/front_fr.54.400.jpg',
               'name': 'coca-cola zéro sucres'},
              {'active': True, 'id_user': 1, 'id_product_fav': 485, 'nutriscore': 'b', 'id_product': 485,
               'url_image': 'https://static.openfoodfacts.org/images/products/350/211/000/9357/front_fr.68.400.jpg',
               'name': 'pepsi max'},
              {'active': True, 'id_user': 1, 'id_product_fav': 623, 'nutriscore': 'b', 'id_product': 623,
               'url_image': 'https://static.openfoodfacts.org/images/products/544/900/021/4799/front_fr.91.400.jpg',
               'name': 'coca cola zéro'},
              {'active': True, 'id_user': 1, 'id_product_fav': 651, 'nutriscore': 'c', 'id_product': 651,
               'url_image': 'https://static.openfoodfacts.org/images/products/366/134/407/0769/front_fr.59.400.jpg',
               'name': 'les 2 vaches vanille de madagascar'},
              {'active': True, 'id_user': 1, 'id_product_fav': 574, 'nutriscore': 'e', 'id_product': 574,
               'url_image': 'https://static.openfoodfacts.org/images/products/544/900/001/1527/front_fr.49.400.jpg',
               'name': 'fanta orange'},
              {'active': True, 'id_user': 1, 'id_product_fav': 650, 'nutriscore': 'c', 'id_product': 650,
               'url_image': 'https://static.openfoodfacts.org/images/products/303/445/000/1123/front_fr.71.400.jpg',
               'name': 'knorr assaisonnement liquide viandox 160ml'},
              {'active': True, 'id_user': 1, 'id_product_fav': 38, 'nutriscore': 'a', 'id_product': 38,
               'url_image': 'https://static.openfoodfacts.org/images/products/730/040/048/1588/front_fr.123.400.jpg',
               'name': 'pain croustillant fibres'},
              {'active': False, 'id_user': 1, 'id_product_fav': 15, 'nutriscore': 'a', 'id_product': 15,
               'url_image': 'https://static.openfoodfacts.org/images/products/501/047/734/8678/front_fr.148.400.jpg',
               'name': 'special muesli 30% fruits & noix céréales complètes'},
              {'active': False, 'id_user': 1, 'id_product_fav': 655, 'nutriscore': 'a', 'id_product': 655,
               'url_image': 'https://static.openfoodfacts.org/images/products/329/207/000/5161/front_fr.91.400.jpg',
               'name': 'houmous extra'}]
    assert req == result
