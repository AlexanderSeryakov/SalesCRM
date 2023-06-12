from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView


urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('new_product/', ProductCreateView.as_view(), name='new_product'),
]
