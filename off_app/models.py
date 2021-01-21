from django.db import models

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


class Category(BaseModel):
    """  """
    name = models.CharField(max_length=100)


class ProductCategory(models.Model):
    """  """
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class User(models.Model):
    """  """
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Favorite(models.Model):
    """ """
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
