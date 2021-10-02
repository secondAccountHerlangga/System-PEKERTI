from django.contrib import admin
from .models import *
from django.apps import apps


# Register your models here.
@admin.register(Peserta)
class Peserta(admin.ModelAdmin):
    list_display = ("nama","nidn","institusi_asal","gelombang","nomer_telp","is_validated","linkSertifikat")

    def Sertifikat(self, obj):
        return bool(obj.linkSertifikat)==True
    
    #displayed
    list_filter = ["is_validated"]
    search_fields = ["nama","nidn","institusi_asal","gelombang","nomer_telp","is_validated"]
    Sertifikat.boolean = True

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass