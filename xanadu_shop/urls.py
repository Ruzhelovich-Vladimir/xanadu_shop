from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('index/', mainapp.main, name='main'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('about/', mainapp.about, name='about'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
