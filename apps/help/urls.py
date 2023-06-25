from django.urls import path
from .views import help_home, about_project


urlpatterns = [
    path('', help_home, name='help'),
    path('about/', about_project, name='about'),
]
