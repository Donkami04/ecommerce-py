from mitienda.models import Category, Product
from mitienda.forms import ProductForm

from django.shortcuts import render, HttpResponse

def categories(request):
    categories = Category.objects.all()
    return render(request, 'mitienda/categories.html', {'categories': categories})

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category_id)
    return render(request,'mitienda/category_products.html', {'category': category, 'products': products})

def create_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Created')
    else:
        form = ProductForm()
    return render(request, 'mitienda/create_product.html', {'form': form})