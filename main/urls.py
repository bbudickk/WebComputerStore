from django.urls import path
from .views import *


urlpatterns = [
    path('', main_page, name="home"),
    path('product/<int:product_id>/', show_product, name="product"),
    path('basket-add/<int:product_id>/', basket_add, name="basket_add"),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
    path('search/', search, name='search'),
]
