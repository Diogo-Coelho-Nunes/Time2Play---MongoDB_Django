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