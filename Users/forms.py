from django.contrib.auth import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class CreateUser(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    last_name=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email=forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control',
    }))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    password1=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    password2=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
        
    def __init__(self,*args,**kwargs):
        super(CreateUser,self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email','password1', 'password2']:
            self.fields[fieldname].help_text=None

