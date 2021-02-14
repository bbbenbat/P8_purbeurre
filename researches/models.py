from django.db import models

from accounts.models import CustomUser


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class Product(BaseModel):
    """  """
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=1000)
    barcode = models.CharField(max_length=20, unique=True)
    ingredient = models.CharField(max_length=3000)
    url_image = models.CharField(max_length=1000, null=True)
    nutriment = models.CharField(max_length=5000)


class Category(BaseModel):
    """  """
    name = models.CharField(max_length=100)


class ProductCategory(BaseModel):
    """  """
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Favorite(BaseModel):
    """ """
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
