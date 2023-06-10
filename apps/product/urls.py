from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView


urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('new_product/', ProductCreateView.as_view(), name='new_product'),
]
