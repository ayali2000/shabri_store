from django.contrib.auth import forms
from django import forms
from . models import *

class UploadfilesForm(forms.ModelForm):
    class Meta:
        model=LearniMaterials
        fields=['Document_name','Course_name','Year','Semester','Document']
        