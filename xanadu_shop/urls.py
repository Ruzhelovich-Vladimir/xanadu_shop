from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static

from mainapp import views as mainapp_viws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_viws.main, name='main'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('about/', mainapp.about, name='about'),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
