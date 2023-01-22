from Time2Playapp.models import *
from django.contrib.auth.hashers import make_password,check_password
from django.db import connections

#Registo
def registo(nome, email, password, tipo, UserStatus):
    if not User.objects.filter(UserEmail=email):
        registo = User(UserName=nome, UserEmail=email, UserPassword=make_password(password), UserType=tipo, UserStatus=UserStatus)
        registo.save()
    else:
        return "Email já existe"

#Login
def login(email, password):
    if User.objects.filter(UserEmail=email):
        user = User.objects.get(UserEmail=email)
        if check_password(password, user.UserPassword) and user.UserType == 'Parceiro' or user.UserType == 'parceiro' and user.UserStatus == True:
            print('dados corretos')
            return 'Parceiro'
        elif check_password(password, user.UserPassword) and user.UserType == 'Admin' or user.UserType == 'admin':
            print('dados corretos')
            return 'Admin'
        elif check_password(password, user.UserPassword) and user.UserType == 'C1' or user.UserType == 'c1':
            print('dados corretos')
            return 'C1'
        elif check_password(password, user.UserPassword) and user.UserType == 'C2' or user.UserType == 'c2':
            print('dados corretos')
            return 'C2'
        elif check_password(password, user.UserPassword) and user.UserType == 'Cliente' or user.UserType == 'cliente':
            return 'Cliente'
        else:
            return False
    else:
        return False

#C1
def addPrdt(nome, descricao, preco,quantidade,imagem,tipo):
    if tipo == '1':
        id = ProductType.objects.get(ProductTypeId=1)
        tipo = id.ProductTypeName
    elif tipo == '2':
        id = ProductType.objects.get(ProductTypeId=2)
        tipo = id.ProductTypeName
    elif tipo == '3':
        id = ProductType.objects.get(ProductTypeId=3)
        tipo = id.ProductTypeName
    elif tipo == '4':
        id = ProductType.objects.get(ProductTypeId=4)
        tipo = id.ProductTypeName
    
    registo = Product(ProductName=nome, ProductDescription=descricao, ProductPrice=preco, ProductQuantity=quantidade, ProductImage=imagem, ProductTypeId=tipo)
    registo.save()

#Admin
def funcao():
    if User.objects.filter(UserStatus='True'):
        return User.objects.filter(UserStatus='True')


def funcao2():
    if User.objects.filter(UserStatus='False'):
        return User.objects.filter(UserStatus='False')