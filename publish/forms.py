from django import forms
from django.forms import ModelForm
from .models import member

class cobaForm(forms.Form):
    nama = forms.CharField(label='nama')
    email = forms.EmailField(label='email')

class lagiForm(ModelForm):
    class Meta:
        model = member
        fields = ['alamat_palsu','name']
