from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    brand_name = models.CharField(max_length=20)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  product_name = models.CharField(max_length=50)
  product_desc = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  price = models.DecimalField(max_digits=5, decimal_places=2)
  stock_no = models.IntegerField()

  def __str__(self):
        return self.product_name
        
class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  pub_date = models.DateTimeField('date published')

class Orderitem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)


