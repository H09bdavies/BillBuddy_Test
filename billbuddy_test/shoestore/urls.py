from django.urls import path

from . import views

app_name='shoestore'
urlpatterns = [
    path('', views.index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('product/<int:product_id>/', views.detail, name='detail'),
    path('brand/<int:brand_name>/', views.detail, name='brands'),
    path('<int:product_id>/buy/', views.buy, name='buy'),
]