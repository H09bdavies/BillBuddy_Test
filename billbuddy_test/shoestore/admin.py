from django.contrib import admin

from .models import Product
from .models import Brand
from .models import Order
from .models import Orderitem

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Order)
admin.site.register(Orderitem)
