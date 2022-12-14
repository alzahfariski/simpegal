from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),    
    path('bantuan/', views.bantuan, name='bantuan'),    
    path('ajukan pengaduan/', views.ajuan, name='ajuan'),    
    path('ajukan pengaduan/<slug:aduanslug>', views.detaduan, name='detaduan'),    
    path('detail berita/<slug:artikelslug>', views.detberita, name='detberita'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)