from django.urls import path

from . import product_category_views, product_name_views, product_views, basket_views

urlpatterns = [
    path('product_category/', product_category_views.product_category_list),
    path('product_category/<int:pk>/', product_category_views.product_category_detail),
    path('product_name/', product_name_views.product_name_list),
    path('product_name/<int:pk>/', product_name_views.product_name_detail),
    path('product/', product_views.product_list),
    path('product/<int:pk>/', product_views.product_detail),
    path('basket/', basket_views.basket_list),
    # path('basket/<int:pk>/', basket_views.basket_detail),
]