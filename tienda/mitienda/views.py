from mitienda.models import Category, Product
from mitienda.forms import ProductForm

from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse

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
            return HttpResponseRedirect(reverse('mitienda:category_products', args=request.POST['category']))

    else:
        form = ProductForm()
    return render(request, 'mitienda/create_product.html', {'form': form})

def delete_product_confirmation(request, product_id):
    object = Product.objects.get(id=product_id)
    return render(request, 'mitienda/delete_product_confirmation.html', {'product': object})

def delete_product(request, product_id):
    object = Product.objects.get(id=product_id)
    object_category = object.category.id
    print('XXXXXXXXXXXXXXXXXXXX ================>',object_category)
    object.delete()
    return render(request, 'mitienda/removed.html', {'product': object})

def modify_product(request, product_id):
    pass