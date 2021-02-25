# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module, via the InfoProd class, give the information for a product.
"""
import ast

import django

from researches.models import Product

django.setup()


class InfoProd:
    """ This class return a dictionary with the information of a product (
    req). """

    def find_product(self, req):
        """ This module gives the information for a product. """
        list_prod = {}
        product = Product.objects.filter(pk=req)
        for loop in product:
            list_prod = {
                'name': loop.name, 'nutriment': loop.nutriment,
                'nutriscore': loop.nutriscore, 'url': loop.url,
                'url_image': loop.url_image, 'barcode': loop.barcode,
                'ingredient': loop.ingredient}
        product_list = list_prod
        product_nutri = product_list['nutriment']
        list_product = ast.literal_eval(product_nutri)
        return list_product, product_list
