# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class Favorites from favorites file. """

from django.test import TestCase

from researches.controllers import favorites
from researches.models import Favorite, Product

favo = favorites.Favorites()

ID_USER = 1


class test_favorites_Favorites(TestCase):
    fixtures = ['fixtures/testdata.json']

    def test_show_favorite(self):
        """ This method allows to find the user's favorite products.
        The user with ID '1'."""
        req = favo.show_favorite(ID_USER)
        result = [{'product': 'pâte à tartiner', 'date': '2021-02-22 17:38',
                   'nutriscore': 'd',
                   'url':
                       'https://fr.openfoodfacts.org/produit/3560070472888'
                       '/pate'
                       '-a-tartiner-carrefour-bio',
                   'id': 2232,
                   'url_image':
                       'https://static.openfoodfacts.org/images/products'
                       '/356/007/047/2888/front_fr.69.400.jpg',
                   'active': False, 'fav_prod': 2232},
                  {'product': 'purée de cacahuètes',
                   'date': '2021-02-22 17:38',
                   'nutriscore': 'b',
                   'url':
                       'https://fr.openfoodfacts.org/produit/3390390000153'
                       '/puree'
                       '-de-cacahuetes-jean-herve',
                   'id': 2830,
                   'url_image':
                       'https://static.openfoodfacts.org/images/products'
                       '/339/039/000/0153/front_fr.130.400.jpg',
                   'active': True, 'fav_prod': 2830}]
        assert req == result

    def test_save_favorite(self):
        """ This method allows to save the user's favorite products.
        The 'id_product' number has not be safe in Favorite table with the
        user
        id."""
        id_product = 2335
        while True:
            check_fav = Favorite.objects.filter(id_product_id=id_product)
            if check_fav:
                id_product += 1
            else:
                break
        favo.save_favorite(id_product, ID_USER)
        req = Favorite.objects.get(id_product_id=id_product,
                                   id_user_id=ID_USER)
        assert req

    def test_update_favorite(self):
        """ Update favorite product statut of the user (active or not). """
        statut = False
        fav_prod = Favorite.objects.filter(id_user_id=ID_USER, active=True)
        for loop in fav_prod:
            id_product = loop.id_product_id
        favo.update_favorite(statut, ID_USER, id_product)
        fav = Favorite.objects.filter(id_user_id=ID_USER,
                                      id_product_id=id_product)
        for loop in fav:
            req = loop.active
        result = statut
        assert req == result

    def test_statut_fav_from_prod(self):
        """ Give the list of product with favorite statement. """
        fav = Favorite.objects.filter(id_user_id=ID_USER).values_list(
            'id_product_id', flat=True)
        prod = Product.objects.filter(pk__in=fav)
        req = favo.statut_fav_from_prod(prod, ID_USER)
        result = [{'active': True, 'id_user': 1, 'id_product_fav': 2830,
                   'nutriscore': 'b', 'id_product': 2830,
                   'url_image':
                       'https://static.openfoodfacts.org/images/products'
                       '/339/039/000/0153/front_fr.130.400.jpg',
                   'name': 'purée de cacahuètes'},
                  {'active': False, 'id_user': 1, 'id_product_fav': 2232,
                   'nutriscore': 'd', 'id_product': 2232,
                   'url_image':
                       'https://static.openfoodfacts.org/images/products'
                       '/356/007/047/2888/front_fr.69.400.jpg',
                   'name': 'pâte à tartiner'}]
        assert req == result
