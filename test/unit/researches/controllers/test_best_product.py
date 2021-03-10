# !/usr/bin/env python
# -*- coding: utf-8 -*-
""" This module test the class BestResearch from best_product file. """
from django.test import TestCase

from researches.controllers import best_product
from researches.models import Product

best_res = best_product.BestResearch()

USER_RESEARCH = 'biscuit'
LIST_CAT = {3984: 18, 3985: 5, 3986: 5, 3987: 18, 3988: 13, 3989: 13, 3995: 1,
            3996: 1, 3997: 1, 3998: 1, 3999: 1, 4000: 1, 4106: 1, 4107: 1,
            4119: 1, 4006: 3, 4002: 1, 4003: 1, 4439: 1, 4440: 1, 4441: 1,
            4442: 1, 4145: 2, 4444: 2, 4445: 2, 4453: 1, 4480: 1, 4071: 1}

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
        result = '[<Product: Product object (3868)>, <Product: Product ' \
                 'object (3874)>, <Product: Product object (3877)>, ' \
                 '<Product: Product object (3903)>, <Product: Product ' \
                 'object (3918)>, <Product: Product object (3925)>, ' \
                 '<Product: Product object (3932)>, <Product: Product ' \
                 'object (3938)>, <Product: Product object (3945)>, ' \
                 '<Product: Product object (3956)>, <Product: Product ' \
                 'object (3960)>, <Product: Product object (3961)>, ' \
                 '<Product: Product object (3965)>, <Product: Product ' \
                 'object (3966)>, <Product: Product object (3990)>, ' \
                 '<Product: Product object (4000)>, <Product: Product ' \
                 'object (4006)>, <Product: Product object (4019)>, ' \
                 '<Product: Product object (4039)>, <Product: Product ' \
                 'object (4051)>, <Product: Product object (4059)>, ' \
                 '<Product: Product object (4060)>, <Product: Product ' \
                 'object (4068)>, <Product: Product object (4077)>, ' \
                 '<Product: Product object (4087)>, <Product: Product ' \
                 'object (4096)>, <Product: Product object (4101)>, ' \
                 '<Product: Product object (4108)>, <Product: Product ' \
                 'object (4126)>, <Product: Product object (4143)>, ' \
                 '<Product: Product object (4145)>, <Product: Product ' \
                 'object (4146)>, <Product: Product object (4158)>, ' \
                 '<Product: Product object (4171)>, <Product: Product ' \
                 'object (4174)>, <Product: Product object (4180)>, ' \
                 '<Product: Product object (4186)>, <Product: Product ' \
                 'object (4191)>, <Product: Product object (4194)>, ' \
                 '<Product: Product object (4199)>, <Product: Product ' \
                 'object (4210)>, <Product: Product object (4585)>, ' \
                 '<Product: Product object (4587)>, <Product: Product ' \
                 'object (4595)>, <Product: Product object (4609)>, ' \
                 '<Product: Product object (4611)>, <Product: Product ' \
                 'object (4612)>, <Product: Product object (4618)>, ' \
                 '<Product: Product object (4621)>, <Product: Product ' \
                 'object (4625)>, <Product: Product object (4633)>, ' \
                 '<Product: Product object (4645)>, <Product: Product ' \
                 'object (4647)>, <Product: Product object (4648)>, ' \
                 '<Product: Product object (4654)>, <Product: Product ' \
                 'object (4671)>, <Product: Product object (4674)>, ' \
                 '<Product: Product object (4691)>, <Product: Product ' \
                 'object (4700)>, <Product: Product object (4704)>, ' \
                 '<Product: Product object (4727)>, <Product: Product ' \
                 'object (4745)>, <Product: Product object (4749)>, ' \
                 '<Product: Product object (4751)>, <Product: Product ' \
                 'object (4774)>, <Product: Product object (4780)>, ' \
                 '<Product: Product object (4784)>, <Product: Product ' \
                 'object (4794)>, <Product: Product object (4802)>, ' \
                 '<Product: Product object (4815)>, <Product: Product ' \
                 'object (4842)>, <Product: Product object (4859)>, ' \
                 '<Product: Product object (4870)>, <Product: Product ' \
                 'object (4873)>, <Product: Product object (4880)>, ' \
                 '<Product: Product object (4883)>, <Product: Product ' \
                 'object (4891)>, <Product: Product object (4895)>, ' \
                 '<Product: Product object (4918)>, <Product: Product ' \
                 'object (4932)>, <Product: Product object (4943)>, ' \
                 '<Product: Product object (4963)>, <Product: Product ' \
                 'object (4988)>, <Product: Product object (4989)>, ' \
                 '<Product: Product object (5016)>, <Product: Product ' \
                 'object (5029)>, <Product: Product object (5061)>, ' \
                 '<Product: Product object (5063)>, <Product: Product ' \
                 'object (5068)>, <Product: Product object (5082)>, ' \
                 '<Product: Product object (5101)>, <Product: Product ' \
                 'object (5103)>, <Product: Product object (5106)>, ' \
                 '<Product: Product object (5112)>, <Product: Product ' \
                 'object (5126)>, <Product: Product object (5158)>, ' \
                 '<Product: Product object (5167)>, <Product: Product ' \
                 'object (5190)>, <Product: Product object (5192)>, ' \
                 '<Product: Product object (5211)>, <Product: Product ' \
                 'object (5240)>, <Product: Product object (5252)>, ' \
                 '<Product: Product object (5263)>, <Product: Product ' \
                 'object (5294)>, <Product: Product object (5301)>, ' \
                 '<Product: Product object (5306)>, <Product: Product ' \
                 'object (5312)>, <Product: Product object (5334)>, ' \
                 '<Product: Product object (5342)>, <Product: Product ' \
                 'object (5349)>, <Product: Product object (5368)>, ' \
                 '<Product: Product object (5369)>, <Product: Product ' \
                 'object (5376)>, <Product: Product object (5386)>, ' \
                 '<Product: Product object (5387)>, <Product: Product ' \
                 'object (5397)>, <Product: Product object (5398)>, ' \
                 '<Product: Product object (5433)>, <Product: Product ' \
                 'object (5447)>, <Product: Product object (5457)>, ' \
                 '<Product: Product object (5463)>, <Product: Product ' \
                 'object (5481)>, <Product: Product object (5484)>, ' \
                 '<Product: Product object (5495)>, <Product: Product ' \
                 'object (5502)>, <Product: Product object (5516)>, ' \
                 '<Product: Product object (5547)>, <Product: Product ' \
                 'object (5552)>, <Product: Product object (5566)>, ' \
                 '<Product: Product object (5580)>, <Product: Product ' \
                 'object (5619)>, <Product: Product object (5646)>, ' \
                 '<Product: Product object (5657)>, <Product: Product ' \
                 'object (5666)>]'
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
