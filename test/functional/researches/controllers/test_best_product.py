""" This module test the class BestResearch from best_product file. """
from researches.controllers import best_product
from researches.models import Product

best_res = best_product.BestResearch()

LIST_CAT = {2447: 2, 2448: 2, 2449: 8, 2450: 2, 2451: 2, 2452: 2, 2453: 2,
            2454: 2, 2455: 2, 2456: 1, 2457: 2, 2458: 4, 2459: 2, 2429: 4,
            2541: 2, 2550: 4, 2648: 2, 2729: 4, 2442: 1, 2470: 1, 2764: 1,
            2644: 2, 2945: 2, 2946: 2}


def test_bestresearch_category_ref():
    """ Find the categories related to the user search. """
    user_research = 'coca'
    result = LIST_CAT
    req = best_res.category_ref(user_research)
    assert req == result


def test_bestresearch_find_best_product():
    """ Find the products with the 3 most frequent categories.  """
    result = '[<Product: Product object (2323)>, <Product: Product object (' \
             '2349)>, <Product: Product object (2831)>, <Product: Product ' \
             'object (2942)>]'
    req = best_res.find_best_product(LIST_CAT)
    assert str(req) == result


def test_bestresearch_list_best_nutri():
    """ Classify a product list according to the nutritional score. """
    prod = Product.objects.filter(
        pk__in=(2025, 2036, 2039, 2067, 2081, 2088, 2095))
    req = best_res.list_best_nutri(prod)
    result = '<QuerySet [<Product: Product object (2067)>, <Product: ' \
             'Product object (2039)>, <Product: Product object (2036)>, ' \
             '<Product: Product object (2025)>, <Product: Product object (' \
             '2081)>, <Product: Product object (2088)>, <Product: Product ' \
             'object (2095)>]>'
    assert str(req) == result


def mock_category_ref(self, req):
    """ Mock the methode 'category_ref' to replace it in
    'test_bestresearch_bestresearch_all'. """
    result = LIST_CAT
    return result


def mock_find_best_product(self, req):
    """ Mock the methode 'best_product' to replace it in
    'test_bestresearch_bestresearch_all'. """
    result = Product.objects.filter(
        pk__in=(3, 135, 453, 485, 510, 519, 574, 623, 733, 754))
    return result


def mock_list_best_nutri(self, req):
    """ Mock the methode 'list_best_nutri' to replace it in
        'test_bestresearch_bestresearch_all'. """
    result = '<QuerySet [<Product: Product object (2067)>, <Product: ' \
             'Product object (2039)>, <Product: Product object (2036)>, ' \
             '<Product: Product object (2025)>, <Product: Product object (' \
             '2081)>, <Product: Product object (2088)>, <Product: Product ' \
             'object (2095)>]>'
    return result


def test_bestresearch_bestresearch_all(monkeypatch):
    """ Find a list of products with the best nutritional
        score according to user research.  """
    user_research = 'biscuit'
    monkeypatch.setattr(
        'researches.controllers.best_product.BestResearch.category_ref',
        mock_category_ref)
    monkeypatch.setattr(
        'researches.controllers.best_product.BestResearch.find_best_product',
        mock_find_best_product)
    monkeypatch.setattr(
        'researches.controllers.best_product.BestResearch.list_best_nutri',
        mock_list_best_nutri)
    req = best_res.bestresearch_all(user_research)
    result = '<QuerySet [<Product: Product object (2067)>, <Product: ' \
             'Product object (2039)>, <Product: Product object (2036)>, ' \
             '<Product: Product object (2025)>, <Product: Product object (' \
             '2081)>, <Product: Product object (2088)>, <Product: Product ' \
             'object (2095)>]>'
    assert str(req) == result
