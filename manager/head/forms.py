from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widget = {
            'name': forms.TextInput()
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'auther': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_auther': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_p_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'retal_period': forms.NumberInput(attrs={'class': 'form-control'}),
           # 'active': forms.BooleanField(attrs={'class': 'form-check-input : form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'catagory': forms.Select(attrs={'class': 'form-control'}),

        }