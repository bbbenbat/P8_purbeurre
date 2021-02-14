""" This module test the class BestResearch from best_product file. """
from researches.controllers import best_product
from researches.models import Product

best_res = best_product.BestResearch()

USER_RESEARCH = 'coca'
LIST_CAT = {1: 4, 14: 4, 15: 7, 16: 4, 17: 2, 18: 2,
            19: 2, 20: 2, 21: 2, 22: 1, 23: 2, 24: 4,
            25: 2, 114: 2, 342: 1, 343: 1, 344: 1, 345: 1,
            346: 1, 219: 2, 539: 2, 540: 2}


def test_bestresearch_category_ref():
    """ Find the categories related to the user search. """

    result = LIST_CAT
    req = best_res.category_ref(USER_RESEARCH)
    assert req == result


def test_bestresearch_find_best_product():
    """ Find the products with the 3 most frequent categories.  """
    result = 'Product object (3)'
    req = best_res.find_best_product(LIST_CAT)
    assert str(req[0]) == result



def test_bestresearch_list_best_nutri():
    """ Classify a product list according to the nutritional score.
     The product with ID '1' has a better nutriscore than the product with ID '10'. """
    ID_PROD = ['10', '11']
    #prod = Product.objects.filter(pk__in=ID_PROD)
    prod = Product.objects.filter(pk__in=(3,135,453,485,510,519,574,623,733,754))
    req = best_res.list_best_nutri(prod)
    print(req)
    """result = ('Product object (11)', 'Product object (10)')
    req = str(req[0]), str(req[1])
    assert req == result"""

#test_bestresearch_list_best_nutri()

def mock_category_ref(self, req):
    """ Mock the methode 'category_ref' to replace it in
    'test_bestresearch_bestresearch_all'. """
    result = LIST_CAT
    return result

def mock_find_best_product(self, req):
    """ Mock the methode 'best_product' to replace it in
    'test_bestresearch_bestresearch_all'. """
    result = Product.objects.filter(pk__in=(3,135,453,485,510,519,574,623,733,754))
    return result

def mock_list_best_nutri(self, req):
    """ Mock the methode 'list_best_nutri' to replace it in
        'test_bestresearch_bestresearch_all'. """
    result = Product.objects.filter(pk__in=(510, 623, 485, 733, 574, 3, 754, 135, 453, 519)).order_by('nutriscore')
    return result


def test_bestresearch_bestresearch_all(monkeypatch):
    """ Find a list of products with the best nutritional
        score according to user research.  """
    monkeypatch.setattr('researches.controllers.best_product.BestResearch.category_ref',
                        mock_category_ref)
    monkeypatch.setattr('researches.controllers.best_product.BestResearch.find_best_product',
                        mock_find_best_product)
    req = best_res.bestresearch_all(USER_RESEARCH)
    result = Product.objects.filter(pk__in=(510,623,485,733,574,3,754,135,453,519)).order_by('nutriscore')
    assert str(req) == str(result)
