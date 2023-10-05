from .models import news
from django import forms
from django.forms import ModelForm

class NewsForm(ModelForm):
    class Meta:
        model=news
        fields="__all__"
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),
            "reporter":forms.TextInput(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class":"form-control"}),
        
        }