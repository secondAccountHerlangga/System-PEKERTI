from djongo import models

# reference https://www.djongomapper.com/using-django-with-mongodb-data-fields/#nesting-embedded-fields
class Permission(models.Model):
    validate_data = models.BooleanField()
    update_data_peserta = models.BooleanField()
    add_other_user =models.BooleanField()

class Admin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    permission = models.EmbeddedField(model_container=Permission)

class Peserta_data(models.Model):
    linkOpenLearning = models.CharField(max_length=50)
    linkAksesKelas = models.CharField(max_length=50)
    linkSertifikat = models.CharField(max_length=50)
    
class Peserta(models.Model):
    nama = models.CharField(max_length=50)
    nidn = NotImplemented
    institusi_asal = NotImplemented
    email = models.EmailField(max_length=254)
    nomer_telp  = models.PhoneNumberField()
    link_transfer = models.CharField( max_length=50)
    link_penugasan = models.CharField(max_length=50)
    link_tidak_menggugat = models.CharField(max_length=50)
    permission = models.EmbeddedField(model_container=Peserta_data)