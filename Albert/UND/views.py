from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):    
    return render(request, 'pages/contact.html')

def collection(request):
    return render(request, 'pages/collection.html')

def signup(request):
    return render(request, 'pages/signup.html')

def login(request):
    return render(request, 'pages/login.html')

def products_list(request):
    products = Product.objects.all()
    return render(request, 'pages/product/list.html', {'products': products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'pages/product/create.html', {'form': form})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    else:
        form = ProductForm(instance=product)

    return render(request, 'pages/product/edit.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product_list')