from django import forms
from .models import artikel,kategori,aduan

class postartikel(forms.ModelForm):
    class Meta:
        model = artikel
        fields = [
            'judul',
            'isi',            
            'sumber',
            'gambar',
        ]

class postkategori(forms.ModelForm):
    class Meta:
        model = kategori
        fields = [
            'nama',
            'sifat',
            'jenis',
        ]

class postaduan(forms.ModelForm):
    class Meta:
        model = aduan
        fields = [
            'nama',
            'jalan',
            'kecamatan',
            'keterangan',
            'status',
        ]