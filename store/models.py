from django.db import models
from catagory.models import Catagory

# Create your models here.


class Product(models.Model):
    product_name        = models.CharField(max_length=100, unique=True)
    slug                = models.SlugField(max_length=200, unique=True)
    description         = models.CharField(max_length=400)
    price               = models.IntegerField()
    images              = models.ImageField(upload_to='products/images')
    stock               = models.IntegerField()
    is_available        = models.BooleanField(default=True)
    catagory            = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name