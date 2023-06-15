from django.urls import path

from . import views

urlpatterns = [
    path('', views.SaleListView.as_view(), name='sales'),
    path('new_sale/', views.SaleCreateView.as_view(), name='new_sale'),
    path('sale/<int:pk>', views.SaleDetailView.as_view(), name='detail'),
    path('sale_update/<int:pk>', views.SaleUpdateView.as_view(), name='sale_update'),
    path('sale_delete/<int:pk>', views.SaleDeleteView.as_view(), name='sale_delete'),


]
