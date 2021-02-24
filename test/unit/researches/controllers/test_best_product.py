# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class BestResearch from best_product file. """
from django.test import TestCase

from researches.controllers import best_product
from researches.models import Product

best_res = best_product.BestResearch()

USER_RESEARCH = 'biscuit'
LIST_CAT = {2442: 17, 2445: 16, 2470: 5, 2471: 5, 2472: 2, 2473: 2,
            2474: 1, 2475: 1, 2443: 11, 2444: 11, 2497: 1,
            2498: 1, 2499: 1, 2500: 1, 2501: 1, 2502: 1,
            2597: 1, 2598: 1, 2611: 1, 2832: 1, 2833: 1,
            2834: 1, 2446: 3, 2935: 1, 2936: 1, 2937: 1,
            2938: 1, 2637: 2, 2940: 2, 2941: 2, 2951: 1,
            2978: 1, 2565: 1}

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
    fixtures = ['fixtures/testdata.json']

    def test_bestresearch_category_ref(self):
        """ Find the categories related to the user search. """
        result = LIST_CAT
        req = best_res.category_ref(USER_RESEARCH)
        assert req == result

    def test_bestresearch_find_best_product(self):
        """ Find the products with the 3 most frequent categories.  """
        result = '[<Product: Product object (2025)>, <Product: Product ' \
                 'object (2036)>, ' \
                 '<Product: Product object (2039)>, <Product: Product ' \
                 'object (2067)>, ' \
                 '<Product: Product object (2081)>, <Product: Product ' \
                 'object (2088)>, ' \
                 '<Product: Product object (2095)>, <Product: Product ' \
                 'object (2102)>, ' \
                 '<Product: Product object (2109)>, <Product: Product ' \
                 'object (2120)>, ' \
                 '<Product: Product object (2124)>, <Product: Product ' \
                 'object (2125)>, ' \
                 '<Product: Product object (2129)>, <Product: Product ' \
                 'object (2130)>, ' \
                 '<Product: Product object (2155)>, <Product: Product ' \
                 'object (2166)>, ' \
                 '<Product: Product object (2172)>, <Product: Product ' \
                 'object (2185)>, ' \
                 '<Product: Product object (2205)>, <Product: Product ' \
                 'object (2217)>, ' \
                 '<Product: Product object (2225)>, <Product: Product ' \
                 'object (2226)>, ' \
                 '<Product: Product object (2235)>, <Product: Product ' \
                 'object (2245)>, ' \
                 '<Product: Product object (2256)>, <Product: Product ' \
                 'object (2265)>, ' \
                 '<Product: Product object (2267)>, <Product: Product ' \
                 'object (2270)>, ' \
                 '<Product: Product object (2277)>, <Product: Product ' \
                 'object (2295)>, ' \
                 '<Product: Product object (2312)>, <Product: Product ' \
                 'object (2314)>, ' \
                 '<Product: Product object (2315)>, <Product: Product ' \
                 'object (2327)>, ' \
                 '<Product: Product object (2340)>, <Product: Product ' \
                 'object (2343)>, ' \
                 '<Product: Product object (2350)>, <Product: Product ' \
                 'object (2356)>, ' \
                 '<Product: Product object (2361)>, <Product: Product ' \
                 'object (2364)>, ' \
                 '<Product: Product object (2369)>, <Product: Product ' \
                 'object (2380)>, ' \
                 '<Product: Product object (2763)>, <Product: Product ' \
                 'object (2765)>, ' \
                 '<Product: Product object (2773)>, <Product: Product ' \
                 'object (2787)>, ' \
                 '<Product: Product object (2789)>, <Product: Product ' \
                 'object (2790)>, ' \
                 '<Product: Product object (2796)>, <Product: Product ' \
                 'object (2800)>, ' \
                 '<Product: Product object (2804)>, <Product: Product ' \
                 'object (2811)>, ' \
                 '<Product: Product object (2823)>, <Product: Product ' \
                 'object (2825)>, ' \
                 '<Product: Product object (2826)>, <Product: Product ' \
                 'object (2832)>, ' \
                 '<Product: Product object (2852)>, <Product: Product ' \
                 'object (2855)>, ' \
                 '<Product: Product object (2872)>, <Product: Product ' \
                 'object (2881)>, ' \
                 '<Product: Product object (2885)>, <Product: Product ' \
                 'object (2908)>, ' \
                 '<Product: Product object (2927)>, <Product: Product ' \
                 'object (2931)>, ' \
                 '<Product: Product object (2933)>, <Product: Product ' \
                 'object (2956)>, ' \
                 '<Product: Product object (2962)>, <Product: Product ' \
                 'object (2966)>, ' \
                 '<Product: Product object (2976)>, <Product: Product ' \
                 'object (2984)>, ' \
                 '<Product: Product object (2989)>, <Product: Product ' \
                 'object (2997)>, ' \
                 '<Product: Product object (3024)>, <Product: Product ' \
                 'object (3041)>, ' \
                 '<Product: Product object (3052)>, <Product: Product ' \
                 'object (3055)>, ' \
                 '<Product: Product object (3062)>, <Product: Product ' \
                 'object (3065)>, ' \
                 '<Product: Product object (3073)>, <Product: Product ' \
                 'object (3077)>, ' \
                 '<Product: Product object (3100)>, <Product: Product ' \
                 'object (3113)>, ' \
                 '<Product: Product object (3124)>, <Product: Product ' \
                 'object (3144)>, ' \
                 '<Product: Product object (3169)>, <Product: Product ' \
                 'object (3170)>, ' \
                 '<Product: Product object (3198)>, <Product: Product ' \
                 'object (3211)>, ' \
                 '<Product: Product object (3243)>, <Product: Product ' \
                 'object (3245)>, ' \
                 '<Product: Product object (3250)>, <Product: Product ' \
                 'object (3264)>, ' \
                 '<Product: Product object (3284)>, <Product: Product ' \
                 'object (3286)>, ' \
                 '<Product: Product object (3289)>, <Product: Product ' \
                 'object (3295)>, ' \
                 '<Product: Product object (3309)>, <Product: Product ' \
                 'object (3341)>, ' \
                 '<Product: Product object (3350)>, <Product: Product ' \
                 'object (3373)>, ' \
                 '<Product: Product object (3375)>, <Product: Product ' \
                 'object (3395)>, ' \
                 '<Product: Product object (3424)>, <Product: Product ' \
                 'object (3436)>, ' \
                 '<Product: Product object (3447)>, <Product: Product ' \
                 'object (3478)>, ' \
                 '<Product: Product object (3486)>, <Product: Product ' \
                 'object (3491)>, ' \
                 '<Product: Product object (3497)>, <Product: Product ' \
                 'object (3519)>, ' \
                 '<Product: Product object (3527)>, <Product: Product ' \
                 'object (3534)>, ' \
                 '<Product: Product object (3553)>, <Product: Product ' \
                 'object (3554)>, ' \
                 '<Product: Product object (3561)>, <Product: Product ' \
                 'object (3571)>, ' \
                 '<Product: Product object (3572)>, <Product: Product ' \
                 'object (3582)>, ' \
                 '<Product: Product object (3583)>, <Product: Product ' \
                 'object (3616)>, ' \
                 '<Product: Product object (3629)>, <Product: Product ' \
                 'object (3639)>, ' \
                 '<Product: Product object (3644)>, <Product: Product ' \
                 'object (3662)>, ' \
                 '<Product: Product object (3665)>, <Product: Product ' \
                 'object (3676)>, ' \
                 '<Product: Product object (3683)>, <Product: Product ' \
                 'object (3696)>, ' \
                 '<Product: Product object (3727)>, <Product: Product ' \
                 'object (3732)>, ' \
                 '<Product: Product object (3746)>, <Product: Product ' \
                 'object (3760)>, ' \
                 '<Product: Product object (3799)>, <Product: Product ' \
                 'object (3826)>, ' \
                 '<Product: Product object (3837)>, <Product: Product ' \
                 'object (3846)>]'
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
        assert str(req) == result
