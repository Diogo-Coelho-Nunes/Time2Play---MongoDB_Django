from contextlib import _RedirectStream, redirect_stderr
from django.shortcuts import render, redirect
from Time2Playapp import database
from Time2Playapp.models import *
from Time2Playapp.database import *
from .forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404

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
            UserStatus = 'False'
        elif request.POST.get('UserType') == 'Admin' or request.POST.get('UserType') == 'admin':
            UserStatus = 'True'
        elif request.POST.get('UserType') == 'C1' or request.POST.get('UserType') == 'c1':
            UserStatus = 'True'
        elif request.POST.get('UserType') == 'C2' or request.POST.get('UserType') == 'c2':
            UserStatus = 'True'
        elif request.POST.get('UserType') == 'Cliente' or request.POST.get('UserType') == 'cliente':
            UserStatus = 'True'
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

#C1
def c1(request):
    context = {}
    return render(request, 'C1_templates/Comercial1_MainPage.html', context = context)

def addPrdt(request):
    if request.method == 'POST':
        # Handle form submission
        form = addPrdtForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('/c1')
    else:
        # Handle GET request
        form = addPrdtForm()
    return render(request, 'C1_templates/InserirProdutos.html', {'form': form})

def listPrdt(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'C1_templates/ListarProdutos.html', context=context)

def addSale(request):
    if request.method == 'POST':
        # Handle form submission
        form = addSaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.save()
            Product.objects.filter(ProductTypeId=Sales.ProductTypeId).update(Product.ProductPrice)
            return redirect('/c1')
    else:
        # Handle GET request
        form = addSaleForm()
    return render(request, 'C1_templates/InserirPromocao.html', {'form': form})

def adm(request):
    context = {}
    return render(request, 'Adm_templates/MainPage.html', context = context)

def aprpar(request):
    if request.method == 'GET':
        users = database.funcao2()
        context = {'users': users}
        return render(request, 'Adm_templates/AprovarUsers.html', context=context)

def criarut(request):
    if request.method == 'POST':
        # Handle form submission
        form = adduserform(request.POST)
        if form.is_valid():
            password = form.cleaned_data['UserPassword']
            password_enc = make_password(password)
            Users = User.objects.create(UserName=form.cleaned_data['UserName'],UserEmail=form.cleaned_data['UserEmail'],UserPassword=password_enc,UserType=form.cleaned_data['UserType'])
            return redirect('/adm')
    else:
        # Handle GET request
        form = adduserform()
    return render(request, 'Adm_templates/CriarUtilizador.html', {'form': form})

def gerirut(request):
    if request.method == 'GET':
        users = database.funcao()
        context = {'users': users}
        return render(request, 'Adm_templates/GerirUtilizadores.html', context=context)

def deleteuser(request, id):
  users = get_object_or_404(User,pk=id)
  users.delete()
  return redirect('/adm/gerirut')

def deleteuserAP(request, id):
    users = get_object_or_404(User,pk=id)
    users.delete()
    return redirect('/adm/aprpar')

def aprovaruser(request,id):
    users = get_object_or_404(User,pk=id)
    print(users.UserStatus)
    users.UserStatus = "True"
    users.save()
    return redirect('/adm/aprpar')

def par(request):
    context = {}
    return render(request, 'Parc_templates/MainPage.html', context = context)

def addPrdtParc(request):
    if request.method == 'POST':
        # Handle form submission
        form = addPrdtFormParc(request.POST,request.FILES)
        if form.is_valid():
            Users = Product.objects.create(ProductName=form.cleaned_data['ProductName'],ProductDescription=form.cleaned_data['ProductDescription'],ProductPrice=form.cleaned_data['ProductPrice'],ProductQuantity=form.cleaned_data['ProductQuantity'],ProductImage=form.cleaned_data['ProductImage'],ProductTypeId=form.cleaned_data['ProductTypeId'],ProductUserId='parceiro')
            return redirect('/par')
    else:
        # Handle GET request
        form = addPrdtFormParc()
    return render(request, 'Parc_templates/CriarProdutos.html', {'form': form})