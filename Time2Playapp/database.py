from Time2Playapp.models import *
from django.contrib.auth.hashers import make_password,check_password
from django.db import connections
from django.db.models import Q

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

def listPartnerPrdt():
    if Product.objects.filter(Q(ProductUserId='Parceiro') | Q(ProductUserId='parceiro')):
        return Product.objects.filter(Q(ProductUserId='Parceiro') | Q(ProductUserId='parceiro'))

def list_client():
    if User.objects.filter(Q(UserType='Cliente') | Q(UserType='cliente') | Q(UserType='Parceiro') | Q(UserType='parceiro')):
        return User.objects.filter(Q(UserType='Cliente') | Q(UserType='cliente') | Q(UserType='Parceiro') | Q(UserType='parceiro'))

def list_orders():
    postgres = connections['second'].cursor()
    #postgres.execute("SELECT * FROM orders")
    postgres.execute("SELECT * FROM orders")
    orders = postgres.fetchall()
    postgres.close()
    return orders
