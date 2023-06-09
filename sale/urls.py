from django.urls import path
from . import views


urlpatterns = [
    path('', views.SaleListView.as_view(), name='sales'),
    path('new_sale/', views.SaleCreateView.as_view(), name='new_sale'),
    path('sale/<int:pk>', views.SaleDetailView.as_view(), name='detail'),
    path('sale_update/<int:pk>', views.SaleUpdateView.as_view(), name='sale_update'),
    path('sale_delete/<int:pk>', views.SaleDeleteView.as_view(), name='sale_delete'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
]
