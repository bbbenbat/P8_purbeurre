# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class Favorites from favorites file. """

from django.test import TestCase

from researches.controllers import favorites
from researches.models import Favorite, Product

favo = favorites.Favorites()

ID_USER = 1


class test_favorites_Favorites(TestCase):
    fixtures = ['fixtures/testdb.json']

    def test_show_favorite(self):
        """ This method allows to find the user's favorite products.
        The user with ID '1'."""
        req = favo.show_favorite(ID_USER)
        result = [
            {'product': 'coca-cola zéro sucres', 'date': '2021-03-12 11:08',
             'nutriscore': 'b',
             'url': 'https://fr.openfoodfacts.org/produit/5000112611762'
                    '/coca-cola-zero-sucres-the-coca-cola-company',
             'id': 587,
             'url_image': 'https://static.openfoodfacts.org/images/products'
                          '/500/011/261/1762/front_fr.54.400.jpg',
             'active': False, 'fav_prod': 587},
            {'product': 'ouf! la pâte à tartiner cacao noisettes',
             'date': '2021-03-12 11:08', 'nutriscore': 'b',
             'url': 'https://fr.openfoodfacts.org/produit/3770008009653/ouf'
                    '-la-pate-a-tartiner-cacao-noisettes-funky-veggie',
             'id': 1244,
             'url_image': 'https://static.openfoodfacts.org/images/products'
                          '/377/000/800/9653/front_fr.63.400.jpg',
             'active': True, 'fav_prod': 1244},
            {'product': 'purée cacahuète', 'date': '2021-03-12 11:08',
             'nutriscore': 'b',
             'url': 'https://fr.openfoodfacts.org/produit/3390390000153'
                    '/puree-cacahuete-jean-herve',
             'id': 698,
             'url_image': 'https://static.openfoodfacts.org/images/products'
                          '/339/039/000/0153/front_fr.136.400.jpg',
             'active': True, 'fav_prod': 698}]

        assert req == result

    def test_save_favorite(self):
        """ This method allows to save the user's favorite products.
        The 'id_product' number has not be safe in Favorite table with the
        user
        id."""
        id_product = 1050
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
        result = [{'active': True, 'id_user': 1, 'id_product_fav': 698,
                   'nutriscore': 'b', 'id_product': 698,
                   'url_image':
                       'https://static.openfoodfacts.org/images/products'
                       '/339/039/000/0153/front_fr.136.400.jpg',
                   'name': 'purée cacahuète'},
                  {'active': False, 'id_user': 1, 'id_product_fav': 587,
                   'nutriscore': 'b', 'id_product': 587,
                   'url_image':
                       'https://static.openfoodfacts.org/images/products'
                       '/500/011/261/1762/front_fr.54.400.jpg',
                   'name': 'coca-cola zéro sucres'},
                  {'active': True, 'id_user': 1, 'id_product_fav': 1244,
                   'nutriscore': 'b', 'id_product': 1244,
                   'url_image': 'https://static.openfoodfacts.org/images/'
                                'products/377/000/800/9653/'
                                'front_fr.63.400.jpg',
                   'name': 'ouf! la pâte à tartiner cacao noisettes'}]
        assert req == result
