from django.shortcuts import render

# Create your views here.
def allProducts(request):
    return render(request, 'product/allProducts.html')


def productDetail(request, name=None):
    return render(request, 'product/productDetail.html')
    
