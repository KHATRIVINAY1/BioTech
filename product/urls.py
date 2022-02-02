from django.urls import path
from .views import allProducts, productDetail, categoryList

urlpatterns = [path('', allProducts, name="allProducts"),
                path('category/<str:category>', categoryList, name="productCategory"),
            path('<slug:slug>/',productDetail, name="productDetail" )
]

