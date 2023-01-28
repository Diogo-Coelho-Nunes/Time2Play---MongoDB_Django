from contextlib import _RedirectStream, redirect_stderr
from django.shortcuts import render, redirect
from Time2Playapp import database
from Time2Playapp.models import *
from Time2Playapp.database import *
from .forms import *
from django.shortcuts import get_object_or_404
import pygal


#import highcharts



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
        elif resultado == resultado:
            request.session['id'] = resultado
            print(request.session['id'])
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
            product = Product.objects.get(ProductTypeId=sale.ProductTypeId)
            product.ProductPrice = product.ProductPrice * (1-(sale.Promotion/100))
            product.save()
            return redirect('/c1')
    else:
        # Handle GET request
        form = addSaleForm()
    return render(request, 'C1_templates/InserirPromocao.html', {'form': form})

def removeSale(request):
    if request.method == 'POST':
        # Handle form submission
        form = removeSaleForm(request.POST)
        if form.is_valid():
            sale = Sales.objects.filter(ProductTypeId=form.cleaned_data['ProductTypeId'])
            for sale in sale:
                try:
                    product = Product.objects.get(ProductTypeId=sale.ProductTypeId)
                    product.ProductPrice = product.ProductPrice / (1-(sale.Promotion/100))
                    product.save()
                    sale.delete()
                except: Product.DoesNotExist
                pass
            return redirect('/c1')
    else:
        # Handle GET request
        form = removeSaleForm()
    return render(request, 'C1_templates/RemoverPromocao.html', {'form': form})

def listPartnerPrdt(request):
    if request.method == 'GET':
        products = database.listPartnerPrdt()
        context = {'products': products}
        return render(request, 'C1_templates/ListarProdutosPartner.html', context=context)

def ChangePrdtStatus(request, ProductId):
    product = get_object_or_404(Product, pk=ProductId)
    if request.method == 'POST':
        form = changeStatusForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/c1')
       
    else:
       form = changeStatusForm(instance=product)
       return render(request, 'C1_templates/AlterarStatusProduto.html', {'form': form})

def count_products(request):
    product_count = Product.objects.filter().count()
    bar_chart = pygal.Bar()
    bar_chart.title = "Product Count"
    bar_chart.add('Product', product_count)
    chart = bar_chart.render_data_uri()
    return render(request, 'C1_templates/count_products.html', {'chart': chart})

def client(request):
    context = {}
    return render(request, 'Clients_templates/Client_main_page.html', context = context)

def categorias(request):
    context = {}
    return render(request, 'Clients_templates/Categorias.html', context = context)

def playstation_list(request):
    products = database.listjogosPS()
    context = {'products': products}
    return render(request,'Clients_templates/PlayStation_list.html',context=context)

def xbox_list(request):
    products = database.listjogosXbox()
    context = {'products': products}
    return render(request,'Clients_templates/Xbox_list.html',context=context)

def pc_list(request):
    products = database.listjogosPC()
    context = {'products': products}
    return render(request,'Clients_templates/PC_list.html',context=context)

def nintendo_list(request):
    products = database.listjogosNintendo()
    context = {'products': products}
    return render(request,'Clients_templates/Nintendo_list.html',context=context)

def perfil(request):
    userid = request.session.get('id')
    user = User.objects.get(pk = userid)
    form = changeperfil(request.POST or None,instance=user)
    if form.is_valid():
        password = form.cleaned_data['UserPassword']
        password_enc = make_password(password)
        Users = User.objects.filter(UserId = userid).update(UserName=form.cleaned_data['UserName'],UserEmail=form.cleaned_data['UserEmail'],UserPassword=password_enc)
            
        return redirect('/cliente')
    
    return render(request, 'Clients_templates/perfil.html', {'form': form})

