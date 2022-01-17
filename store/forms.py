from django.contrib.auth import forms
from django import forms
from . models import *

class Ordeform(forms.ModelForm):
    Address=forms.CharField(widget=forms.Textarea(attrs={
        'rows':3,
        'cols':25
        }))
    class Meta:
        model=Order
        fields=['Phone_Number','quantity','Address']

