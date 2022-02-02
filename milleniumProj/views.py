
from django.shortcuts import render, redirect
from product.models import Category
from django.core.paginator import Paginator

from product.models import Product
def homepage(request):
    all_categories = Category.objects.all()
    on_sale_products = Product.objects.filter(featured=True)

    return render(request, 'index.html', {'all_categories':all_categories, 'on_sale_products':on_sale_products})

def searchProduct(request):
    product = request.GET.get('query')
    query= product
    products = Product.objects.all().filter(name__icontains=product)
    paginator = Paginator(products, 10) # Show 10 posts per page.
    page_number = request.GET.get('page',1)
    products = paginator.get_page(page_number)
    return render(request, 'product/allProducts.html',{'products': products, 'query':query}) 


