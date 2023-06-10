from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('apps.sale.urls')),
                  path('analytics/', include('apps.analytics.urls'))
                ]


if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
