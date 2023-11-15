from django import forms
from .models import UploadedZip

class ZipUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedZip
        fields = ['zip_file']
