from django.urls import path
from . import views


urlpatterns = [
    path('', views.SalesPageView.as_view(), name='sales'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
]
