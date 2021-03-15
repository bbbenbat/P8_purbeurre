""" This module test the class SaveDataApi from save_data_api file. """

from researches.controllers import save_data_api
from researches.models import Product, Category

save_data = save_data_api.SaveDataApi()


def test_save_products():
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
    req = Product.objects.get(name='test')
    Product.objects.filter(name__in=('test', 'test2')).delete()
    Category.objects.filter(name='test categories').delete()
    assert req
