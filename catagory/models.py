from django.db import models

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to="products/images", blank=True)

    class Meta():
        verbose_name = 'catagory'
        verbose_name_plural = "catagories"

    def __str__(self):
        return self.catagory_name
