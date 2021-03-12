# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class BestResearch from best_product file. """
from django.test import TestCase

from researches.controllers import best_product
from researches.models import Product

best_res = best_product.BestResearch()

USER_RESEARCH = 'biscuit'
LIST_CAT = {42: 18, 43: 5, 44: 5, 45: 18, 46: 13, 47: 13, 53: 1, 54: 1, 55: 1,
            56: 1, 57: 1, 58: 1, 161: 1, 162: 1, 174: 1, 64: 3, 60: 1, 61: 1,
            498: 1, 499: 1, 500: 1, 501: 1, 200: 2, 503: 2, 504: 2, 512: 1,
            538: 1, 126: 1}

PROD_FILT = (
    2025, 2036, 2039, 2067, 2081, 2088, 2095, 2102, 2109, 2120, 2124,
    2125, 2129, 2130, 2155, 2166, 2172, 2185, 2205, 2217, 2225, 2226,
    2235, 2245, 2256, 2265, 2267, 2270, 2277, 2295, 2312, 2314, 2315,
    2327, 2340, 2343, 2350, 2356, 2361, 2364, 2369, 2380, 2763, 2765,
    2773, 2787, 2789, 2790, 2796, 2800, 2804, 2811, 2823, 2825, 2826,
    2832, 2852, 2855, 2872, 2881, 2885, 2908, 2927, 2931, 2933, 2956,
    2962, 2966, 2976, 2984, 2989, 2997, 3024, 3041, 3052, 3055, 3062,
    3065, 3073, 3077, 3100, 3113, 3124, 3144, 3169, 3170, 3198, 3211,
    3243, 3245, 3250, 3264, 3284, 3286, 3289, 3295, 3309, 3341, 3350,
    3373, 3375, 3395, 3424, 3436, 3447, 3478, 3486, 3491, 3497, 3519,
    3527, 3534, 3553, 3554, 3561, 3571, 3572, 3582, 3583, 3616, 3629,
    3639, 3644, 3662, 3665, 3676, 3683, 3696, 3727, 3732, 3746, 3760,
    3799, 3826, 3837, 3846)


class MyTest(TestCase):
    # Must live in <your_app>/fixtures/data.json
    fixtures = ['fixtures/testdb.json']

    def test_bestresearch_category_ref(self):
        """ Find the categories related to the user search. """
        result = LIST_CAT
        req = best_res.category_ref(USER_RESEARCH)
        assert req == result

    def test_bestresearch_find_best_product(self):
        """ Find the products with the 3 most frequent categories.  """
        result = '[<Product: Product object (9)>, <Product: Product object ' \
                 '(15)>, <Product: Product object (18)>, <Product: Product ' \
                 'object (43)>, <Product: Product object (58)>, <Product: ' \
                 'Product object (65)>, <Product: Product object (72)>, ' \
                 '<Product: Product object (78)>, <Product: Product object ' \
                 '(85)>, <Product: Product object (96)>, <Product: Product ' \
                 'object (100)>, <Product: Product object (101)>, <Product: ' \
                 'Product object (105)>, <Product: Product object (106)>, ' \
                 '<Product: Product object (130)>, <Product: Product object ' \
                 '(140)>, <Product: Product object (146)>, <Product: ' \
                 'Product object (159)>, <Product: Product object (179)>, ' \
                 '<Product: Product object (191)>, <Product: Product object ' \
                 '(199)>, <Product: Product object (200)>, <Product: ' \
                 'Product object (208)>, <Product: Product object (217)>, ' \
                 '<Product: Product object (227)>, <Product: Product object ' \
                 '(236)>, <Product: Product object (241)>, <Product: ' \
                 'Product object (248)>, <Product: Product object (267)>, ' \
                 '<Product: Product object (551)>, <Product: Product object ' \
                 '(553)>, <Product: Product object (554)>, <Product: ' \
                 'Product object (566)>, <Product: Product object (579)>, ' \
                 '<Product: Product object (582)>, <Product: Product object ' \
                 '(588)>, <Product: Product object (594)>, <Product: ' \
                 'Product object (599)>, <Product: Product object (602)>, ' \
                 '<Product: Product object (607)>, <Product: Product object ' \
                 '(618)>, <Product: Product object (631)>, <Product: ' \
                 'Product object (633)>, <Product: Product object (641)>, ' \
                 '<Product: Product object (655)>, <Product: Product object ' \
                 '(657)>, <Product: Product object (658)>, <Product: ' \
                 'Product object (664)>, <Product: Product object (667)>, ' \
                 '<Product: Product object (671)>, <Product: Product object ' \
                 '(679)>, <Product: Product object (691)>, <Product: ' \
                 'Product object (693)>, <Product: Product object (694)>, ' \
                 '<Product: Product object (700)>, <Product: Product object ' \
                 '(717)>, <Product: Product object (720)>, <Product: ' \
                 'Product object (737)>, <Product: Product object (746)>, ' \
                 '<Product: Product object (750)>, <Product: Product object ' \
                 '(773)>, <Product: Product object (791)>, <Product: ' \
                 'Product object (795)>, <Product: Product object (797)>, ' \
                 '<Product: Product object (820)>, <Product: Product object ' \
                 '(826)>, <Product: Product object (830)>, <Product: ' \
                 'Product object (840)>, <Product: Product object (848)>, ' \
                 '<Product: Product object (853)>, <Product: Product object ' \
                 '(861)>, <Product: Product object (888)>, <Product: ' \
                 'Product object (905)>, <Product: Product object (916)>, ' \
                 '<Product: Product object (919)>, <Product: Product object ' \
                 '(926)>, <Product: Product object (929)>, <Product: ' \
                 'Product object (937)>, <Product: Product object (941)>, ' \
                 '<Product: Product object (964)>, <Product: Product object ' \
                 '(978)>, <Product: Product object (989)>, <Product: ' \
                 'Product object (1009)>, <Product: Product object (1034)>, ' \
                 '<Product: Product object (1035)>, <Product: Product ' \
                 'object (1062)>, <Product: Product object (1075)>, ' \
                 '<Product: Product object (1106)>, <Product: Product ' \
                 'object (1108)>, <Product: Product object (1113)>, ' \
                 '<Product: Product object (1127)>, <Product: Product ' \
                 'object (1147)>, <Product: Product object (1149)>, ' \
                 '<Product: Product object (1152)>, <Product: Product ' \
                 'object (1158)>, <Product: Product object (1172)>, ' \
                 '<Product: Product object (1204)>, <Product: Product ' \
                 'object (1213)>, <Product: Product object (1236)>, ' \
                 '<Product: Product object (1238)>, <Product: Product ' \
                 'object (1257)>, <Product: Product object (1286)>, ' \
                 '<Product: Product object (1298)>, <Product: Product ' \
                 'object (1309)>, <Product: Product object (1340)>, ' \
                 '<Product: Product object (1347)>, <Product: Product ' \
                 'object (1352)>]'
        req = best_res.find_best_product(LIST_CAT)
        assert str(req) == result


def test_bestresearch_list_best_nutri(self):
    """ Classify a product list according to the nutritional score.
     The product with ID '1' has a better nutriscore than the product
     """
    prod = Product.objects.filter(
        pk__in=(2025, 2036, 2039, 2067, 2081, 2088, 2095))
    req = best_res.list_best_nutri(prod)
    result = '<QuerySet [<Product: Product object (2067)>, <Product: ' \
             'Product object (2039)>, ' \
             '<Product: Product object (2036)>, ' \
             '<Product: Product object (2025)>, <Product: Product ' \
             'object (2081)>, <Product: Product object (2088)>, ' \
             '<Product: Product object (2095)>]>'
    print("list_best_nutri", req)
    assert str(req) == result
