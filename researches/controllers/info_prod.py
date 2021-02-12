"""  """
import ast

from researches.models import Product


class InfoProd:
    """  """

    def find_product(self, req):
        """  """
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
