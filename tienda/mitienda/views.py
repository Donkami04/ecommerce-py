from mitienda.models import Category, Product

from django.shortcuts import render

def categories(request):
    categories = Category.objects.all()
    return render(request, 'mitienda/categories.html', {'categories': categories})

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category_id)
    return render(request,'mitienda/category_products.html', {'category': category, 'products': products})
