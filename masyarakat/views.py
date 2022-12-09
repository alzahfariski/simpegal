from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from petugas import models
# Create your views here.
def beranda(request):    
    context={}
    if request.user.is_staff == 0:
        posts = models.artikel.objects.all()
        kategori = models.kategori.objects.all()
        pengaduan = models.aduan.objects.all()
        context={
            'posts': posts,
            'kategori':kategori,
            'pengaduan':pengaduan,
        }       
        return render(request, 'mas/beranda.html',context)
    elif request.user.is_staff == 1:
        return render(request,'eror_404.html' )

def bantuan(request):
    context={}
    if request.user.is_staff == 0:
        return render(request, 'mas/bantuanmas.html', context)
    elif request.user.is_staff == 1:
        return render(request,'eror_404.html' )

def ajuan(request):
    context={}
    if request.user.is_staff == 0: 
        kategori = models.kategori.objects.all()
        context={
            'kategori':kategori,
        }     
        return render(request, 'mas/ajukan.html', context)
    elif request.user.is_staff == 1:
        return render(request,'eror_404.html' )

def detberita(request,artikelslug):
    if request.user.is_staff == 0: 
        posts = models.artikel.objects.get(slug=artikelslug)
        context={
            'page_title':'detail berita',
            'posts':posts,
        }     
        return render(request, 'mas/detberita.html', context)
    elif request.user.is_staff == 1:
        return render(request,'eror_404.html' )


