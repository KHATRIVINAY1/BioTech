from django.urls import path
from .views import allProducts, productDetail

urlpatterns = [path('', allProducts, name="allProducts"),
path('product/<str:name>/',productDetail, name="productDetail" )
]
