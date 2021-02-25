# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module, via the SaveDataApi class, save the product in database.
product. """
import django

django.setup()

from researches.controllers import parser_off
from researches.models import Category, Product, ProductCategory

pars_off = parser_off.ParserOff()


class SaveDataApi():
    """ This class saves products and their categories in the database """

    def save_products(self, req):
        """ Save name, nutriscore, url, barcode, ingredient,url_image,
        nutriment into Product table. """
        for var in req:
            print("TEST :::::::",var)
            try:
                product_name = var['product_name'].lower()
                Product(name=product_name,
                        nutriscore=var['nutrition_grades_tags'][0],
                        url=var['url'], barcode=var['code'],
                        ingredient=var['ingredients_text_fr'],
                        url_image=var['image_front_url'],
                        nutriment=var['nutriments']).save()
                product_id = Product.objects.get(name=product_name)
                # save categories
                cat = var['categories'].split(',')
                # list washing
                cat_clean = pars_off.global_parser(cat)
                # time to save (or not)
                for var1 in cat_clean:
                    # check if category exist
                    if Category.objects.filter(name=var1).exists():
                        pass
                    else:
                        Category(name=var1).save()
                # take categories id db
                cat_id = Category.objects.filter(name__in=cat_clean)
                # take all id into list_id_cat
                for req in cat_id:
                    ProductCategory(id_category_id=req.id,
                                    id_product_id=product_id.id).save()
            except Exception as d:
                pass
