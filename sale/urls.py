from django.urls import path
from . import views


urlpatterns = [
    path('', views.SalesPageView.as_view(), name='sales'),
]
