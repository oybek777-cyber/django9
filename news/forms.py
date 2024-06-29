from django import forms
from .models import Contact


class DataFrom(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','message']
