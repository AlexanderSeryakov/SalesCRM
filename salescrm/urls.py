from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.sale.urls')),
    path('auth/', include('apps.user_auth.urls')),
    path('analytics/', include('apps.analytics.urls')),
    path('product/', include('apps.product.urls')),
]


if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
