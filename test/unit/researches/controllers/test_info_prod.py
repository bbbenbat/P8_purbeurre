# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class InfoProd from info_prod file. """

from django.test import TestCase

from researches.controllers import info_prod

info_p = info_prod.InfoProd()

ID_USER = 1


class test_info_prod_InfoProd(TestCase):
    fixtures = ['fixtures/testdb.json']

    def test_find_product(self):
        """ This module gives the information for a product. """
        id_product = 1050
        req = info_p.find_product(id_product)
        result = ({'energy-kcal_value': 360, 'carbohydrates_serving': 16.8,
                   'fat_100g': 14, 'saturated-fat': 2.5,
                   'carbon-footprint-from-known-ingredients_100g': 105.18,
                   'energy-kj_value': 1510, 'nova-group': 4,
                   'fiber_unit': 'g', 'nutrition-score-fr_100g': 7,
                   'sodium_serving': 0.105, 'nova-group_100g': 4,
                   'proteins_unit': 'g', 'carbohydrates': 48.1,
                   'energy_unit': 'kJ', 'fat_value': 14, 'sodium_unit': 'g',
                   'salt_serving': 0.263, 'fruits-vegetables-nuts': 0,
                   'carbohydrates_value': 48.1, 'fat_unit': 'g',
                   'saturated-fat_serving': 0.875, 'sodium_100g': 0.3,
                   'proteins_100g': 7.9, 'fruits-vegetables-nuts_value': 0,
                   'energy-kcal': 360, 'fiber_100g': 5, 'energy_value': 1510,
                   'proteins_serving': 2.77, 'energy-kj': 1510,
                   'nova-group_serving': 4, 'nutrition-score-fr': 7,
                   'carbon-footprint-from-known-ingredients_serving': 36.8,
                   'sugars_unit': 'g', 'saturated-fat_100g': 2.5,
                   'energy': 1510, 'sodium': 0.3, 'fiber_value': 5,
                   'proteins_value': 7.9,
                   'fruits-vegetables-nuts-estimate-from-ingredients_100g':
                       8.3,
                   'energy-kcal_100g': 360, 'sugars_serving': 5.6,
                   'energy-kj_unit': 'kJ', 'energy-kcal_unit': 'kcal',
                   'energy_serving': 528, 'saturated-fat_unit': 'g',
                   'carbohydrates_100g': 48.1, 'saturated-fat_value': 2.5,
                   'fiber': 5, 'fruits-vegetables-nuts_serving': 0,
                   'carbohydrates_unit': 'g', 'sugars_value': 16,
                   'energy-kcal_serving': 126, 'fat_serving': 4.9,
                   'fruits-vegetables-nuts_unit': 'g',
                   'carbon-footprint-from-known-ingredients_product': 221,
                   'energy-kj_serving': 528, 'proteins': 7.9,
                   'salt_unit': 'g', 'salt': 0.75, 'energy-kj_100g': 1510,
                   'salt_value': 0.75, 'fat': 14, 'energy_100g': 1510,
                   'sugars': 16, 'sugars_100g': 16, 'salt_100g': 0.75,
                   'fruits-vegetables-nuts_100g': 0, 'fiber_serving': 1.75,
                   'sodium_value': 0.3}, {
                      'name': 'harrys brioche mini tressee nature au sucre '
                              'perle',
                      'nutriment': "{'energy-kcal_value': 360, "
                                   "'carbohydrates_serving': 16.8, "
                                   "'fat_100g': 14, 'saturated-fat': 2.5, "
                                   "'carbon-footprint-from-known-ingredients_"
                                   "100g': 105.18, 'energy-kj_value': 1510, "
                                   "'nova-group': 4, 'fiber_unit': 'g', "
                                   "'nutrition-score-fr_100g': 7, "
                                   "'sodium_serving': 0.105, "
                                   "'nova-group_100g': 4, "
                                   "'proteins_unit': 'g', "
                                   "'carbohydrates': 48.1, "
                                   "'energy_unit': 'kJ', "
                                   "'fat_value': 14, "
                                   "'sodium_unit': 'g', "
                                   "'salt_serving': 0.263, "
                                   "'fruits-vegetables-nuts': 0, "
                                   "'carbohydrates_value': 48.1, "
                                   "'fat_unit': 'g', "
                                   "'saturated-fat_serving': 0.875, "
                                   "'sodium_100g': 0.3, 'proteins_100g': "
                                   "7.9, 'fruits-vegetables-nuts_value': 0, "
                                   "'energy-kcal': 360, 'fiber_100g': 5, "
                                   "'energy_value': 1510, "
                                   "'proteins_serving': 2.77, 'energy-kj': "
                                   "1510, 'nova-group_serving': 4, "
                                   "'nutrition-score-fr': 7, "
                                   "'carbon-footprint-from-"
                                   "known-ingredients_serving': 36.8, "
                                   "'sugars_unit': 'g', "
                                   "'saturated-fat_100g': 2.5, 'energy': "
                                   "1510, 'sodium': 0.3, 'fiber_value': 5, "
                                   "'proteins_value': 7.9, "
                                   "'fruits-vegetables-nuts-estimate-"
                                   "from-ingredients_100g': 8.3, "
                                   "'energy-kcal_100g': 360, "
                                   "'sugars_serving': 5.6, "
                                   "'energy-kj_unit': 'kJ', "
                                   "'energy-kcal_unit': 'kcal', "
                                   "'energy_serving': 528, "
                                   "'saturated-fat_unit': 'g', "
                                   "'carbohydrates_100g': 48.1, "
                                   "'saturated-fat_value': 2.5, 'fiber': 5, "
                                   "'fruits-vegetables-nuts_serving': 0, "
                                   "'carbohydrates_unit': 'g', "
                                   "'sugars_value': 16, "
                                   "'energy-kcal_serving': 126, "
                                   "'fat_serving': 4.9, "
                                   "'fruits-vegetables-nuts_unit': 'g', "
                                   "'carbon-footprint-from-known-"
                                   "ingredients_product': 221, "
                                   "'energy-kj_serving': 528, 'proteins': "
                                   "7.9, 'salt_unit': 'g', 'salt': 0.75, "
                                   "'energy-kj_100g': 1510, 'salt_value': "
                                   "0.75, 'fat': 14, 'energy_100g': 1510, "
                                   "'sugars': 16, 'sugars_100g': 16, "
                                   "'salt_100g': 0.75, "
                                   "'fruits-vegetables-nuts_100g': 0, "
                                   "'fiber_serving': 1.75, 'sodium_value': "
                                   "0.3}",
                      'nutriscore': 'c',
                      'url':
                          'https://fr.openfoodfacts.org/produit/'
                          '3228857000661/harrys-brioche-mini-tressee'
                          '-nature-au-sucre-perle',
                      'url_image':
                          'https://static.openfoodfacts.org/images/products'
                          '/322/885/700/0661/front_fr.39.400.jpg',
                      'barcode': '3228857000661',
                      'ingredient': "Farine de blé 48,0%, eau, oeufs frais "
                                    "12,1%, huile de colza, sucre 8,3%, "
                                    "sucre perlé 4,1% (sucre, graisse "
                                    "végétale : karité, arôme), sirop de "
                                    "glucose-fructose, émulsifiant : mono - "
                                    "et diglycérides d'acides gras, arômes "
                                    "dont fleur d'oranger (contient "
                                    "alcool), extraits végétaux à pouvoir "
                                    "colorant (curcuma, paprika), levure, "
                                    "épaississant : gomme de guar, fibre de "
                                    "blé, sel, gluten de blé. peut contenir "
                                    "des traces de lait, graines de sésame, "
                                    "fruits a coque et soja."})

        assert req == result
