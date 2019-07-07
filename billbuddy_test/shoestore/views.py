from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .models import Brand

def index(request):
  newest_products_list = Product.objects.order_by('-pub_date')
  brand_list = Brand.objects.all()
  context = {'newest_products_list': newest_products_list, 'brand_list': brand_list}
  return render(request, 'shoestore/index.html', context)

def brands(request, brand):
  brand_products_list = Product.objects.filter(brand=brand).order_by('-pub_date')
  context = {'brand_products_list': brand_products_list}
  return render(request, 'shoestore/brands.html', context)

def detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  context = {'product': product}
  return render(request, 'shoestore/detail.html', context)