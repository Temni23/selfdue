from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from coolsite import settings
from women.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls', namespace='women')),
]

if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL, document_root =
    settings.MEDIA_ROOT)

handler404 = page_not_found
