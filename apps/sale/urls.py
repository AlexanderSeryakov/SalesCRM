from django.urls import path

from . import views

urlpatterns = [
    path('', views.SaleListView.as_view(), name='sales'),
    path('test/', views.TestView.as_view(), name='test'),
    path('new_sale/', views.SaleCreateView.as_view(), name='new_sale'),
    path('sale/<int:pk>', views.SaleDetailView.as_view(), name='detail'),
    path('sale_update/<int:pk>', views.SaleUpdateView.as_view(), name='sale_update'),
    path('sale_delete/<int:pk>', views.SaleDeleteView.as_view(), name='sale_delete'),

    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
]
