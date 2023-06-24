from django.urls import path
from .views import help_home


urlpatterns = [
    path('', help_home, name='help')
]
