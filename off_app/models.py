from django.db import models


class Product(models.Model):
    """  """
    name = models.CharField(max_length=100)
    nutriscore = models.CharField(max_length=1)
    url = models.CharField(max_length=300)
    barcode = models.CharField(max_length=20, unique=True)
    ingredient = models.CharField(max_length=1000)
    url_image = models.CharField(max_length=1000, null=True)


class Category(models.Model):
    """  """
    name = models.CharField(max_length=100)


class ProductCategory(models.Model):
    """  """
    id_product = models.PositiveIntegerField(null=False)
    id_category = models.PositiveIntegerField(null=False)


class User(models.Model):
    """  """
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=500)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Favorite(models.Model):
    """ """
    date = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField(null=False)
    id_product = models.IntegerField(null=False)
