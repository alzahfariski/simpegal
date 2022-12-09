from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.index,name='home'),    
    path('petugas/',include('petugas.urls')),
    path('auntentifikasi/',include('auntentifikasi.urls')),
    path('beranda/', include('masyarakat.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
