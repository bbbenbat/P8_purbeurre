""" This module test the class Favorites from best_product file. """

from researches.controllers import favorites
from researches.models import Favorite

favo = favorites.Favorites()

def no_test_show_favorite():
    """ This method allows to find the user's favorite products.
    The user with ID '14' has 4 favorite products with ID: """
    user_id = 1
    req = favo.show_favorite(user_id)
    result = {'product': 'schweppes agrumes', 'date': '2021-02-14 13:51', 'nutriscore': 'd', 'url': 'https://fr.openfoodfacts.org/produit/3124480002501/schweppes-agrumes', 'id': 733, 'url_image': 'https://static.openfoodfacts.org/images/products/312/448/000/2501/front_fr.149.400.jpg', 'active': False, 'fav_prod': 733}
    assert req[0] == result

def no_test_save_favorite():
    """ This method allows to save the user's favorite products. """
    id_product = 651
    id_user = 1
    save_fav = favo.save_favorite(id_product,id_user)
    req = Favorite.objects.get(pk = save_fav.pk)
    assert req


