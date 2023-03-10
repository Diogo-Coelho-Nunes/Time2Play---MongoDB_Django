from django import forms
from django.forms import ModelForm
from .models import *


class addPrdtForm(ModelForm):
    class Meta:
        model = Product
        fields = ('ProductName', 'ProductDescription', 'ProductPrice', 'ProductQuantity', 'ProductImage', 'ProductTypeId', 'ProductUserId')
        labels = {
            'ProductName': 'Nome do Produto',
            'ProductDescription': 'Descrição do Produto',
            'ProductPrice': 'Preço do Produto',
            'ProductQuantity': 'Quantidade do Produto',
            'ProductImage': 'Imagem do Produto',
            'ProductTypeId': 'Tipo do Produto',
            'ProductUserId': 'Vendedor',
        }
        widgets = {
            'ProductName': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductDescription': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductQuantity': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductImage': '',
            'ProductTypeId': forms.Select(attrs={'class': 'form-control'}, choices=ProductType.objects.all().values_list('ProductTypeId', 'ProductTypeName')),
            'ProductUserId': forms.TextInput(attrs={'class': 'form-control'}),
        }

class addSaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ('ProductTypeId', 'Promotion')
        labels = {
            'ProductTypeId': 'Tipo de Produto',
            'Promotion': 'Promoção',
        }
        widgets = {
            'ProductTypeId': forms.Select(attrs={'class': 'form-control'}, choices=ProductType.objects.all().values_list('ProductTypeId', 'ProductTypeName')),
            'Promotion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class removeSaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['ProductTypeId']
        labels = {
            'ProductTypeId': 'Tipo de Produto'
        }
        widgets = {
            'ProductTypeId': forms.Select(attrs={'class': 'form-control'}, choices=ProductType.objects.all().values_list('ProductTypeId', 'ProductTypeName'))
        }

class changeStatusForm(ModelForm):
    class Meta:
        model = Product
        fields = ['ProductStatus']
        labels = {
            'ProductStatus': 'Estado do Produto'
        }
        widgets = {
            'ProductStatus': forms.Select(attrs={'class': 'form-control'}, choices=[(True, 'True'), (False, 'False')])
        }

class adduserform(ModelForm):
    class Meta:
        model = User
        fields = ('UserName', 'UserEmail', 'UserPassword', 'UserType')
        labels = {
            'UserName': 'Nome ',
            'UserEmail': 'Email ',
            'UserPassword': 'Password ',
            'UserType': 'Tipo de Utilizador',
        }
        widgets = {
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'UserEmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'UserPassword': forms.PasswordInput(attrs={'class': 'form-control'}),
            'UserType': forms.TextInput(attrs={'class': 'form-control'}),
        }

class addPrdtFormParc(ModelForm):
    class Meta:
        model = Product
        fields = ('ProductName', 'ProductDescription', 'ProductPrice', 'ProductQuantity', 'ProductImage', 'ProductTypeId')
        labels = {
            'ProductName': 'Nome do Produto',
            'ProductDescription': 'Descrição do Produto',
            'ProductPrice': 'Preço do Produto',
            'ProductQuantity': 'Quantidade do Produto',
            'ProductImage': 'Imagem do Produto',
            'ProductTypeId': 'Tipo do Produto',
            'ProductUserId': 'Vendedor',
        }
        widgets = {
            'ProductName': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductDescription': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductQuantity': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductImage': '',
            'ProductTypeId': forms.Select(attrs={'class': 'form-control'}, choices=ProductType.objects.all().values_list('ProductTypeId', 'ProductTypeName')),
        }


class editPrdtFormParc(ModelForm):
    class Meta:
        model = Product
        fields = ('ProductName', 'ProductDescription', 'ProductPrice', 'ProductQuantity')
        labels = {
            'ProductName': 'Nome do Produto',
            'ProductDescription': 'Descrição do Produto',
            'ProductPrice': 'Preço do Produto',
            'ProductQuantity': 'Quantidade do Produto',
            'ProductImage': 'Imagem do Produto',
            'ProductTypeId': 'Tipo do Produto',
            'ProductUserId': 'Vendedor',
        }
        widgets = {
            'ProductName': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductDescription': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductPrice': forms.TextInput(attrs={'class': 'form-control'}),
            'ProductQuantity': forms.TextInput(attrs={'class': 'form-control'}),
        }

class changeperfil(ModelForm):
    class Meta:
        model = User
        fields = ('UserName', 'UserEmail', 'UserPassword')
        labels = {
           'UserName': 'Nome',
           'UserEmail': 'Email',
           'UserPassword':'PassWord',
        }
        widgets = {
            'UserName': forms.TextInput(attrs={'class': 'form-control'}),
            'UserEmail': forms.TextInput(attrs={'class': 'form-control'}),
            'UserPassword': forms.PasswordInput(attrs={'class': 'form-control'}),
            
        }