from django.db.models.fields import DateField
from djongo import models

# class Peserta_data(models.Model):

class Peserta(models.Model):
    _id = models.ObjectIdField()
    nama = models.CharField(max_length=50)
    nidn = models.CharField(max_length=10)
    institusi_asal = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    gelombang = models.DateField(auto_now=False, auto_now_add=False)
    nomer_telp  = models.CharField(("NOMER TELEPON"),max_length=50)
    link_transfer = models.CharField( max_length=50)
    link_penugasan = models.CharField(max_length=50)
    link_kesanggupan = models.CharField(max_length=50)
    is_validated = models.BooleanField(("Status Validasi"))
    linkOpenLearning = models.CharField(
        blank=True,
        max_length=50
    )

    linkAksesKelas = models.CharField(
        blank=True,
        max_length=50
    )

    linkSertifikat = models.CharField(
        ("Sertifikat"),
        blank=True,
        max_length=50
    )


    class Meta:
        verbose_name_plural = "Data Peserta"
    

    
    