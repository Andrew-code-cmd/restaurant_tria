from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:id>', views.product),
    path('product_delete/<int:id>', views.delete),
    path('product_delete_one/<int:id>', views.delete_one),
    path('product_add_one/<int:id>', views.add_one),
    path('salat/<int:id>', views.salat),
    path('fish/<int:id>', views.fish),
    path('soup/<int:id>', views.soup),
    path('zal/', views.zal, name='zal'),
    path('ver/', views.ver, name='ver'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('order/', views.order, name='order'),
]