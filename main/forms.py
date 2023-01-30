from django import forms
from .models import Category, Item


class CategoryFileUploadForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description', 'user', 'photo')


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'user', 'file')