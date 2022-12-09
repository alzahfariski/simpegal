# Register your models here.
from django.contrib import admin

# Register your models here.
from . import models

class artikeladmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'tanggal',
    ]

class aduanadmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'tanggal',
    ]

admin.site.register(models.artikel, artikeladmin)
admin.site.register(models.kategori)
admin.site.register(models.aduan, aduanadmin)


