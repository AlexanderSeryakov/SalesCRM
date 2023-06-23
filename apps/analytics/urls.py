from django.urls import path

from .views import AnalyticsView

urlpatterns = [
    path('', AnalyticsView.as_view(), name='analytics'),
]
