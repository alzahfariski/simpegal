# Generated by Django 3.2 on 2022-12-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petugas', '0003_pengaduan'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengaduan',
            name='status',
            field=models.CharField(choices=[('proses', 'Proses'), ('konfirmasi', 'Konfirmasi'), ('tolak', 'Tolak')], default='proses', max_length=50),
        ),
    ]
