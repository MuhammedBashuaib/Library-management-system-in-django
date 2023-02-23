from django import forms
from .models import *

class FrmBook(forms.ModelForm):
    #start class FrmAddBook
    class Meta:
        #start class Mate
        model = Book
        fields = [
            'title',
            'author',
            'photoBook',
            'photoAuthor',
            'pages',
            'price',
            'rentalPriceDay',
            'rentalPeriod',
            'totalRental',
            'status',
            'category',
        ]
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'author': forms.TextInput(attrs= {'class': 'form-control'}),
            'photoBook': forms.FileInput(attrs= {'class': 'form-control'}),
            'photoAuthor': forms.FileInput(attrs= {'class': 'form-control'}),
            'pages': forms.NumberInput(attrs= {'class': 'form-control'}),
            'price': forms.NumberInput(attrs= {'class': 'form-control'}),
            'rentalPriceDay': forms.NumberInput(attrs= {'class': 'form-control', 'id': 'rentalPrice'}),
            'rentalPeriod': forms.NumberInput(attrs= {'class': 'form-control', 'id': 'rentalDays'}),
            'totalRental': forms.NumberInput(attrs= {'class': 'form-control', 'id': 'totalRental'}),
            'status': forms.Select(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'}),
        }
        #end class Meta
    #end class FrmAddBook

class FrmCategory(forms.ModelForm):
    #start class FrmAddCategory
    class Meta:
        #start class FrmAddMeta
        model = Category
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
        }
        #end class Meta
    #end class FrmAddCategory