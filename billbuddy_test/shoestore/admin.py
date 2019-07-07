from django.contrib import admin

from .models import Product
from .models import Brand

admin.site.register(Product)
admin.site.register(Brand)
# Register your models here.
