from django.urls import path

from . import views

app_name = "mitienda"

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    
]