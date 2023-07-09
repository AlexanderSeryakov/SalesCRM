from django.urls import path
from .views import add_new_supply, SupplyListView, SupplyDetailView
from .api.views import SupplyApiView


urlpatterns = [
    path('', SupplyListView.as_view(), name='supply'),
    path('new_supply/', add_new_supply, name='new_supply'),
    path('detail/<int:pk>', SupplyDetailView.as_view(), name='supply_detail'),
    path('api/v1/supply/', SupplyApiView.as_view(), name='api_supply')
]
