from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def index(request):
  newest_products_list = Product.objects.order_by('-pub_date')
  context = {'newest_products_list': newest_products_list}
  return render(request, 'shoestore/index.html', context)

def detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  context = {'product': product}
  return render(request, 'shoestore/detail.html', context)