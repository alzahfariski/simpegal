from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from petugas import models
from petugas import forms
# Create your views here.
def beranda(request):    
    context={}
    if request.user.is_staff == 0:
        posts =  models.artikel.objects.all()
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
    if request.user.is_staff == 0: 
        post_aduan = forms.postaduan()
        if request.method == 'POST':
            post_aduan = forms.postaduan(request.POST, request.FILES)
            if post_aduan.is_valid():
                post_aduan.save()
                return redirect('beranda')
        context={
            'post_aduan':post_aduan,
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


