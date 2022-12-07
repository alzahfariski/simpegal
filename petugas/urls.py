from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.dashboard_admin, name='dashboard_admin'),    
    path('berita/', views.berita, name='berita_admin'),    
    path('berita/detail_berita/<slug:artikelslug>', views.detail_berita, name='detail_berita'),
    path('berita/tambah_berita/',views.tambah_berita, name='tambah_berita'),
    path('berita/edit_berita/<int:id>',views.edit_berita, name='edit_berita'),
    path('berita/hapus_berita/<delete_id>',views.hapusberita, name='hapusberita'),
    path('kategori/',views.kategori,name='kategori_admin'),
    path('konfirmasi/',views.konfirmasi,name='konfirmasi_admin'),
    path('konfirmasi/detail_konfirmasi/',views.detail_konfirmasi,name='detail_konfirmasi'),
    path('pengaduan/', views.pengaduan,name='pengaduan_admin'),
    path('pengaduan/detail_pengaduan', views.detail_pengaduan, name='detail_pengaduan'),
    path('surat/', views.surat , name='surat_admin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)