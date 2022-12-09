from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from petugas import models


def index(request):
    kategori = models.kategori.objects.all()
    berita = models.artikel.objects.all()    
    context={
        'page_title': 'simpegal',
        'berita':berita,
        'kategori' : kategori,
    }
    return render(request, 'index.html',context)

