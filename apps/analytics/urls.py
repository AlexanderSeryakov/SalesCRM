from django.urls import path

from .views import analytics_view, view_period

urlpatterns = [
    path('', analytics_view, name='analytics'),
    path('view_period/', view_period, name='view_period'),
]
