from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
import datetime
from django.conf import settings
from django.utils.timezone import make_aware

from .models import *

def index(request):
  newest_products_list = Product.objects.order_by('-pub_date')
  brand_list = Brand.objects.all()
  context = {'newest_products_list': newest_products_list, 'brand_list': brand_list}
  return render(request, 'shoestore/index.html', context)
  
def basket(request):
  order = Order.objects.filter(user = request.user)
  print(order)
  orderitem_list = Orderitem.objects.filter(order = order[0])
  context = {'orderitem_list': orderitem_list}
  return render(request, 'shoestore/basket.html', context)

def brands(request, brand):
  brand_products_list = Product.objects.filter(brand=brand).order_by('-pub_date')
  context = {'brand_products_list': brand_products_list}
  return render(request, 'shoestore/brands.html', context)

def detail(request, product_id):
  product = Product.objects.get(pk=product_id)
  context = {'product': product}
  return render(request, 'shoestore/detail.html', context)

def createorder(request):
  settings.TIME_ZONE
  try:
    ordercheck = Order.objects.get(user = request.user)
    return ordercheck
  except:
    order = Order(user = request.user, pub_date = make_aware(datetime.datetime.now()))
    order.save()
    return order

def buy(request, product_id):
  product = get_object_or_404(Product, pk=product_id)
  orderitem = Orderitem(product = product, order = createorder(request))
  orderitem.save()
  return HttpResponseRedirect(reverse('shoestore:index'))

# from https://wsvincent.com/django-user-authentication-tutorial-signup/
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'