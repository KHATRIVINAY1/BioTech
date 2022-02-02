from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


# Create your views here.
def allProducts(request):
    products= Product.objects.all().order_by('-published_date')
    paginator = Paginator(products, 10) # Show 10 posts per page.
    page_number = request.GET.get('page',1)
    products = paginator.get_page(page_number)
    return render(request, 'product/allProducts.html', {'products': products}) 

def categoryList(request, category):
    category = category.replace("-", " ")
    products= Product.objects.prefetch_related('categories').filter(categories__name__icontains=category)
    current_category = category
    paginator = Paginator(products, 10) # Show 10 posts per page.
    page_number = request.GET.get('page',1)
    products = paginator.get_page(page_number)
    return render(request, 'product/allProducts.html',{'products': products, 'current_category':current_category}) 


def productDetail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/productDetail.html', {'product':product})
    