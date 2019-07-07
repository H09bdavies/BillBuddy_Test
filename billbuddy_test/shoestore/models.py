from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=20)

class Product(models.Model):
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  product_name = models.CharField(max_length=50)
  product_desc = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  price = models.DecimalField(max_digits=5, decimal_places=2)
  stock_no = models.IntegerField()

