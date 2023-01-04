from django.urls import path

from . import views

app_name = "mitienda"

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('products/new/', views.create_product, name='create_product'),
    path('products/modify/', views.modify_product, name='modify_product'),
    path('products/delete/<int:product_id>/', views.delete_product_confirmation, name='delete_product_confirmation'),
    path('products/delete/confirmation/<int:product_id>/', views.delete_product, name='delete_product'),
]