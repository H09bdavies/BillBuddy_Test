from django.db import models

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

