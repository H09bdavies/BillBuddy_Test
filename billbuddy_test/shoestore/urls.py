from django.urls import path

from . import views

app_name='shoestore'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('brand/<int:brand_name>/', views.detail, name='brands'),
    path('<int:product_id>/buy/', views.buy, name='buy'),
]