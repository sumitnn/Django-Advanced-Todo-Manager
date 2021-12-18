from django.forms import ModelForm
from . models import *
from django import forms


class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title here...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }


class AddForm(ModelForm):
    class Meta:
        model = Addpost
        fields = ['event_name', 'data', 'location', 'image']
