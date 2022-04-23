# Django Imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.shortcuts import redirect

# Standard Package Imports

# Project Imports
from . import settings

# Third Party Imports


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main'), name='main'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
