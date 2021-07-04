from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #importo los direc.estaticos
from django.conf import settings # importo el archivo settings del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('caosNews.urls')),
    path('',include('api.urls')),
]
# incluto en el path la ubicacion del directorio MEDIA
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)