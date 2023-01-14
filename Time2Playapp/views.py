from contextlib import _RedirectStream, redirect_stderr
from django.shortcuts import render, redirect
from Time2Playapp import database
from Time2Playapp.models import *
from Time2Playapp.database import *

# Create your views here.
def MainPage(request):
    context = {}
    return render(request, 'MainPage.html', context = context)

#Create Users
def popularUser(request):
    if request.method == 'POST':
        nome = request.POST.get('UserName')
        email = request.POST.get('UserEmail')
        password = request.POST.get('UserPassword')
        tipo = request.POST.get('UserType')
        if request.POST.get('UserType') == 'Parceiro' or request.POST.get('UserType') == 'parceiro':
            UserStatus = False
        elif request.POST.get('UserType') == 'Admin' or request.POST.get('UserType') == 'admin':
            UserStatus = True
        elif request.POST.get('UserType') == 'C1' or request.POST.get('UserType') == 'c1':
            UserStatus = True
        elif request.POST.get('UserType') == 'C2' or request.POST.get('UserType') == 'c2':
            UserStatus = True
        elif request.POST.get('UserType') == 'Cliente' or request.POST.get('UserType') == 'cliente':
            UserStatus = True
        resultado = database.registo(nome, email, password, tipo, UserStatus)
        if resultado :
            print('Registo efetuado com sucesso!')
            return redirect('MainPage')
        else:
            print('Erro no registo!')
    context = {}
    return render(request, 'registo.html', context = context)


#Logins
def login(request):
    if request.method == 'POST':
        email = request.POST.get('UserEmail')
        password = request.POST.get('UserPassword')
        resultado = database.login(email, password)
        if resultado == 'Parceiro':
            print('Login efetuado com sucesso!')
            return redirect('/par')
        elif resultado == 'Admin':
            print('Login efetuado com sucesso!')
            return redirect('/adm')
        elif resultado == 'C1':
            print('Login efetuado com sucesso!')
            return redirect('/c1')
        elif resultado == 'C2':
            print('Login efetuado com sucesso!')
            return redirect('/c2')
        elif resultado == 'Cliente':
           print('Login efetuado com sucesso!')
           return redirect('/cliente')
    context = {}
    return render(request, 'login.html', context = context)