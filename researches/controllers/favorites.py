# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module contains the Favorite class, allowing to find and save the
user's favorite products. """
import django

from researches.models import Favorite, Product

django.setup()


class Favorites:
    """ This class allows to find and save the user's favorite products. """

    def show_favorite(self, r_user):
        """ This method allows to find the user's favorite products. """
        favorites = Favorite.objects.filter(id_user=r_user).order_by('-date')
        list_prod = []
        for req in favorites:
            prod = Product.objects.filter(pk=req.id_product_id)
            for req1 in prod:
                date_prod = str(req.date)
                list_prod.append({
                    'product': req1.name, 'date': date_prod[0:16],
                    'nutriscore': req1.nutriscore, 'url': req1.url,
                    'id': req1.id, 'url_image': req1.url_image,
                    'active': req.active, 'fav_prod': req.id_product_id})
        return list_prod

    def save_favorite(self, r_product, r_user):
        """ This method allows to save the user's favorite products. """
        check_favorite = Favorite.objects.filter(id_user_id=r_user,
                                                 id_product_id=r_product)
        if check_favorite:
            save_fav = self.update_favorite(True, r_user, r_product)
        else:
            save_fav = Favorite(id_product_id=r_product,
                                id_user_id=r_user).save()
        return save_fav

    def update_favorite(self, r_statut, r_user, r_product):
        """ Update favorite product statut of the user (active or not). """
        save_fav = Favorite.objects.filter(id_user_id=r_user,
                                           id_product_id=r_product).update(
            active=r_statut)
        return save_fav

    def statut_fav_from_prod(self, r_product, r_user):
        """ Give the list of product with favorite statement. """
        list_prod = []
        for loop in r_product:
            favorite = Favorite.objects.filter(id_user_id=r_user,
                                               id_product_id=loop.pk)
            if favorite:
                for loop1 in favorite:
                    list_prod.append({
                        'active': loop1.active, 'id_user': loop1.id_user_id,
                        'id_product_fav': loop1.id_product_id,
                        'nutriscore': loop.nutriscore, 'id_product': loop.id,
                        'url_image': loop.url_image, 'name': loop.name, })
                    break
            else:
                list_prod.append({
                    'active': None, 'id_user': None, 'id_product_fav': None,
                    'nutriscore': loop.nutriscore, 'id_product': loop.id,
                    'url_image': loop.url_image, 'name': loop.name, })
        return list_prod
