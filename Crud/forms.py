from django import forms
from Crud.models import crudst

class stform(forms.ModelForm):
    class Meta:
        model = crudst
        fields="__all__"