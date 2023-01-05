from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 

from. import views

from . import views

app_name = "mitienda"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='mitienda/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='mitienda/logout.html'), name='logout'),
    
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('products/new/', views.create_product, name='create_product'),
    path('products/modify/<int:product_id>/', views.modify_product, name='modify_product'),
    path('products/update/<int:product_id>/', views.update_product, name='update_product'), # !
    path('products/delete/<int:product_id>/', views.delete_product_confirmation, name='delete_product_confirmation'),
    path('products/delete/confirmation/<int:product_id>/', views.delete_product, name='delete_product'),
]