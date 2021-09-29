from django import forms
from django.forms.widgets import CheckboxInput

class Forms_login(forms.Form):
    username = forms.CharField(
        required=True,
        label="Username",
        max_length = 200
    )
    password = forms.PasswordInput(
        required=True,
        label="password"
    )

class Forms_register(forms.Form):
    nama_lengkap = forms.CharField(
        required=True,
        label="Nama Lengkap Peserta" 
    )
    nidn = forms.CharField( 
        required=True,
        label="NIDN" 
    )
    institusi_asal = forms.CharField( 
        required=True,
        label="Institusi Asal" 
    )
    email = forms.EmailField( 
        required=True,
        label="E-mail" 
    )
    nomer_telp = forms.NumberInput( 
        required=True,
        label="Nomer Telepon Genggam ( dapat dihubungi )" 
    )
    bukti_transfer = forms.FileInput( 
        required=True,
        label="Upload Bukti Transfer" 
    )
    surat_penugasan = forms.FileInput( 
        required=True,
        label="Upload Surat Penugasan Dari Institusi Terkait" 
    )
    surat_tidak_menggugat = forms.FileInput( 
        required=True,
        label="Upload Surat Tidak Menggugat Pengembalian Uang" 
    )

class Form_Validasi(forms.Form):
    is_valid = forms.CheckboxInput( 
        label="Apakah data Valid ?" 
    )

