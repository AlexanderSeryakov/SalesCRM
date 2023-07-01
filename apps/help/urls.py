from django.urls import path

from .views import about_project, help_home, help_license

urlpatterns = [
    path('', help_home, name='help'),
    path('about/', about_project, name='about'),
    path('license/', help_license, name='license')
]
