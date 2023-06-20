from django.urls import path

from .views import home, view_period

urlpatterns = [
    path('', home, name='analytics'),
    path('view_period/', view_period, name='view_period'),
]
