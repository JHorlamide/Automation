from django.db import models


# Create your models here.
# =====================================================
# The single source of information of our product data
# =====================================================
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)



