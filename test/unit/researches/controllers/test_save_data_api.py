# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class SaveDataApi from save_data_api file. """
import django

django.setup()
from django.test import TestCase

from researches.controllers import save_data_api
from researches.models import Product

save_data = save_data_api.SaveDataApi()


class test_save_data_api_SaveDataApi(TestCase):
    fixtures = ['fixtures/testdb.json']

    def test_save_products(self):
        """  """
        prod = ({'product_name': 'test', 'nutrition_grades_tags': 'a',
                 'url': 'http://url.test.com', 'code': '1000001',
                 'ingredients_text_fr': 'ingredient1, ingredient2',
                 'image_front_url': 'http://url_image.test.com',
                 'nutriments': 'nutriment1, nutriment2',
                 'categories': 'Test Categories'},
                {'product_name': 'test2', 'nutrition_grades_tags': 'b',
                 'url': 'http://url.test.com', 'code': '1000002',
                 'ingredients_text_fr': 'ingredient1, ingredient2',
                 'image_front_url': 'http://url_image.test.com',
                 'nutriments': 'nutriment1, nutriment2',
                 'categories': 'Test Categories'}
                )
        save_data.save_products(prod)
        req = Product.objects.filter(name='test')
        assert req
