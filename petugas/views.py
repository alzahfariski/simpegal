from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth.decorators import login_required
from . import models
from .forms import postartikel,postkategori
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
def dashboard_admin(request):    
    context={}
    if request.user.is_staff == 1:
        return render(request, 'admin/dashboard.html',context)
    else:
        return render(request,'eror_404.html')

def berita(request):    
    if request.user.is_staff == 1:
        posts = models.artikel.objects.all()
        context={
            'page_title': 'berita',
            'posts': posts,
        }        
        return render(request, 'admin/berita.html', context)
    else:
        return render(request,'eror_404.html')

def detail_berita(request, artikelslug):
    if request.user.is_staff == 1:
        posts = models.artikel.objects.get(slug=artikelslug)
        context={
            'page_title':'detail berita',
            'posts':posts,
        }
        return render(request, 'admin/detail_berita.html', context)
    else:
        return render(request,'eror_404.html')

def tambah_berita(request):    
    if request.user.is_staff == 1:
        post_artikel = postartikel()        
        if request.method =='POST':
            post_artikel = postartikel(request.POST, request.FILES)           
            if post_artikel.is_valid():                               
                post_artikel.save()
                return redirect ('berita_admin')                             
        context={
            'page_title':'tambah berita',
            'post_artikel':post_artikel,         
        }        
        return render(request, 'admin/tambah_berita.html', context)
    else:
        return render(request,'eror_404.html')

def edit_berita(request, id):
    if request.user.is_staff == 1:
        berita = models.artikel.objects.get(id=id)
        data = {
            'judul':berita.judul,
            'isi':berita.isi,
            'sumber':berita.sumber,
            'gambar':berita.gambar,
        }
        form = postartikel(request.POST or None, request.FILES or None, initial=data, instance=berita)
        if request.method =='POST':
            if form.is_valid():                               
                form.save()
                return redirect ('berita_admin') 
        context = {            
            'form':form,
            'berita':berita,
        }
        return render(request, 'admin/edit_berita.html', context)
    else:
        return render(request,'eror_404.html')

def hapusberita(request, delete_id):    
    models.artikel.objects.filter(id = delete_id).delete()        
    return redirect ('berita_admin')

def kategori(request):
    if request.user.is_staff == 1:
        posts = models.kategori.objects.all()
        post_kategori = postkategori()        
        if request.method =='POST':
            post_kategori = postkategori(request.POST)           
            if post_kategori.is_valid():                               
                post_kategori.save()
                return redirect ('kategori_admin')                             
        context={
            'page_title':'kategori',
            'post_kategori':post_kategori,  
            'posts':posts,       
        }        
        return render(request, 'admin/kategori.html', context)
    else:
        return render(request,'eror_404.html')

def edit_kategori(request, id):
    if request.user.is_staff == 1:
        kategori = models.kategori.objects.get(id = id)
        data = {
            'nama':kategori.nama,
            'sifat':kategori.sifat,
            'jenis':kategori.jenis,        
        }
        form = postkategori(request.POST or None, initial=data, instance=kategori)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('kategori_admin')
        context = {
            'form':form,
            'kategori':kategori,
        }
        return render(request,'admin/edit_kategori.html', context)
    else:
        return render(request,'eror_404.html')

def hapuskategori(request, delete_id):
    models.kategori.objects.filter(id = delete_id).delete()
    return redirect('kategori_admin')


def konfirmasi(request):
    context={}
    if request.user.is_staff == 1:
        return render(request, 'admin/konfirmasi.html', context)
    else:
        return render(request,'eror_404.html')
   
def pengaduan(request):
    context={}
    if request.user.is_staff == 1:
        return render(request, 'admin/pengaduan.html', context)
    else:
        return render(request,'eror_404.html')

  


def detail_pengaduan(request):
    context={}
    if request.user.is_staff == 1:
        return render(request, 'admin/detail_pengaduan.html',context)
    else:
        return render(request,'eror_404.html')

def detail_konfirmasi(request):
    context={}
    if request.user.is_staff == 1:
        return render(request, 'admin/detail_konfirmasi.html')
    else:
        return render(request,'eror_404.html')