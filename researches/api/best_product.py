"""
"""
import django

django.setup()

from researches.models import Product, ProductCategory, Favorite


class BestResearch:
    """  """

    def category_ref(self, req):
        """  """
        list_cat = {}
        list_prod_cat = []
        list_product = Product.objects.filter(name__contains=req)[:20]
        for req in list_product:
            # take the id_category for each product
            list_prod_cat = (ProductCategory.objects.filter(id_product=req.pk).values_list('id_category_id', flat=True))
            for req1 in list_prod_cat:
                if req1 in list_cat:
                    list_cat[req1] += 1
                else:
                    list_cat[req1] = 1
        return list_cat

    def find_best_product(self, req):
        """  """
        list_cat = req
        list_cat_id = sorted(list_cat.items(), key=lambda t: t[1], reverse=True)[:3]
        super_product_a = []
        super_product_b = []
        list_super_cat = []
        best_product = []
        for req in list_cat_id:
            list_super_cat.append(req[0])
        super_product = (ProductCategory.objects.filter(id_category=list_super_cat[0]))
        for req in super_product:
            super_product_a += ProductCategory.objects.filter(id_category=list_super_cat[1],
                                                              id_product=req.id_product).distinct()
        for req in super_product_a:
            super_product_b += ProductCategory.objects.filter(id_category=list_super_cat[2],
                                                              id_product=req.id_product).distinct()
        for req in super_product_b:
            best_product.append(Product.objects.get(pk=req.id_product_id))
        return best_product

    def list_best_nutri(self, req):
        """  """
        list_id = []
        list = req
        for req in list:
            list_id.append(req.id)
        list_product = Product.objects.filter(pk__in=list_id).order_by('nutriscore')
        return list_product

    def bestresearch_all(self, req):
        """  """
        cat = self.category_ref(req)
        find = self.find_best_product(cat)
        list = self.list_best_nutri(find)
        return list



