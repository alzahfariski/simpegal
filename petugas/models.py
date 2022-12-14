from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from auntentifikasi.models import UserProfileInfo
from django.contrib.auth.models import User

# Create your models here.
class artikel(models.Model):
    judul = models.CharField(max_length=250)
    isi = models.TextField()
    tanggal = models.DateField(auto_now_add=True)
    sumber = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='berita/')    
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['-id']

    def save(self):
        self.slug=slugify(self.judul)
        super(artikel,self).save() 

    def __str__(self):
        return self.judul

class kategori(models.Model):
    nama = models.CharField(max_length=100)
    sifat = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.nama

class aduan(models.Model):
    nama = models.CharField(max_length=100)
    jalan = models.CharField(max_length=200)
    kecamatan = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=300)
    foto  = models.ImageField(upload_to='pengaduan/')
    tanggal = models.DateField(auto_now_add=True)    
    status = models.CharField(max_length=50, default='proses')
    kategori_id = models.ForeignKey(kategori,  on_delete=models.CASCADE)
    pengadu_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['-id']

    def save(self):
        self.slug=slugify(self.nama)
        super(aduan,self).save() 

    def __str__(self):
        return self.nama