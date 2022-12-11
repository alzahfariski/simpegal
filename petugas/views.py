from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import models
from .forms import postartikel,postkategori, postaduan
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy

from django.template.loader import get_template
from xhtml2pdf import pisa

# cetak pdf
def cetak_surat(request, *args, **kwargs):
    pk = kwargs.get('pk')
    aduan = get_object_or_404(models.aduan, pk=pk)

    template_path = 'admin/surat.html'
    context = {'aduan': aduan}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # kalo download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # kalo display
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Create your views here.
def dashboard_admin(request): 
    if request.user.is_staff == 1:
        posts = models.aduan.objects.all()
        context = {
            'posts':posts,
            'total_pengaduan':len(models.aduan.objects.all()),
            'total_konfirmasi':len(models.aduan.objects.filter(status = 'konfirmasi')),
            'total_proses':len(models.aduan.objects.filter(status = 'proses')),
            'total_tolak':len(models.aduan.objects.filter(status = 'tolak')),
        }
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

def pengaduan(request):
    if request.user.is_staff == 1:
        posts = models.aduan.objects.all()
        context = {
            'page_title': 'pengaduan',
            'posts': posts,
        }
        return render(request, 'admin/pengaduan.html', context)
    else:
        return render(request,'eror_404.html')

def detail_pengaduan(request, id):
    if request.user.is_staff == 1:
        posts = models.aduan.objects.get(id =id)
        data = {
            'nama':posts.nama,
            'jalan':posts.jalan,
            'kecamatan':posts.kecamatan,
            'keterangan':posts.keterangan,
            'status':posts.status,
        }
        form = postaduan(request.POST or None, request.FILES or None, initial=data, instance=posts)
        if request.method =='POST':
            if form.is_valid():                               
                form.save()
                return redirect ('pengaduan_admin') 
        context={
            'page_title':'detail berita',
            'form':form,
            'posts':posts,
        }
        return render(request, 'admin/detail_pengaduan.html',context)
    else:
        return render(request,'eror_404.html') 

def hapusaduan(request, delete_id):    
    models.aduan.objects.filter(id = delete_id).delete()        
    return redirect ('tolak')       

def konfirmasi(request):
    if request.user.is_staff == 1:
        posts = models.aduan.objects.all()
        context = {
            'page_title': 'konfirmasi',
            'posts': posts,
        }
        return render(request, 'admin/konfirmasi.html', context)
    else:
        return render(request,'eror_404.html')  

def detail_konfirmasi(request):
    context={}
    if request.user.is_staff == 1:
        return render(request, 'admin/detail_konfirmasi.html')
    else:
        return render(request,'eror_404.html')

def tolak(request):
    if request.user.is_staff == 1:
        posts = models.aduan.objects.all()
        context = {
            'posts':posts
        }
        return render(request, 'admin/tolak.html', context)
    else:
        return render(request, 'eror_404.html')