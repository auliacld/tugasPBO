from django.core import validators
from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nama_barang', 'jumlah_barang', 'harga_barang']
        widgets = {
            'nama_barang': forms.TextInput(attrs={'class':'form-control'}),
            'harga_barang': forms.TextInput(attrs={'class':'form-control'}),
            'jumlah_barang': forms.TextInput(attrs={'class':'form-control'}),
        }
