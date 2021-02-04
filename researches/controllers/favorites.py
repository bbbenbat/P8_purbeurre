"""  """
from researches.models import Favorite, Product


class Favorites:
    """  """

    def show_favorite(self, req):
        """  """
        favorites = Favorite.objects.filter(id_user=req)
        list_prod = []
        for req in favorites:
            prod = Product.objects.filter(pk=req.id_product_id)
            for req1 in prod:
                list_prod.append({'product': req1.name, 'date': str(req.date)})
        return list_prod

    def save_favorite(self, req1, req2):
        Favorite(id_product_id=req1, id_user_id=req2).save()