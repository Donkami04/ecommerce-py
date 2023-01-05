from mitienda.models import Category, Product
from mitienda.forms import ProductForm, UserRegistrationForm

from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    categories = Category.objects.all()
    return render(request, 'mitienda/base.html', {'categories': categories})

def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category_id)
    return render(request,'mitienda/category_products.html', {'category': category, 'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mitienda:category_products', args=request.POST['category']))
    else:
        form = ProductForm()
    return render(request, 'mitienda/create_product.html', {'form': form})

def delete_product_confirmation(request, product_id):
    object = Product.objects.get(id=product_id)
    return render(request, 'mitienda/delete_product_confirmation.html', {'product': object})

def delete_product(request, product_id):
    object = Product.objects.get(id=product_id)
    object.delete()
    return render(request, 'mitienda/removed.html', {'product': object})

def modify_product(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    return render(request, 'mitienda/modify_product.html', {'form': form, 'product': product})
    
def update_product(request, product_id):  
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mitienda:category_products', args=request.POST['category']))
        else:
            form = ProductForm(instance=product)
            return render(request,'mitienda/modify_product.html', {'form':form})
        
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido registrado.')
            return redirect('mitienda:home')
            #return render(request, 'mitienda/categories')    
    else:
        form = UserRegistrationForm()
        
    return render(request,'mitienda/register.html', {'form': form})