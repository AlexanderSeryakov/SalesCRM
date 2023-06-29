from django.urls import path

from .views import about_project, help_home

urlpatterns = [
    path('', help_home, name='help'),
    path('about/', about_project, name='about'),
]
