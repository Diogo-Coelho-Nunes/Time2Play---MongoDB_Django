from contextlib import _RedirectStream, redirect_stderr
import datetime
from django.shortcuts import render, redirect
from Time2Playapp import database
from Time2Playapp.models import *
from Time2Playapp.database import *
from .forms import *
from django.shortcuts import get_object_or_404
import pygal
from django.core import serializers 
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
def MainPage(request):
    if request.method == 'GET':
        products = Product.objects.order_by('ProductPrice')[:6]
        context = {'products': products}
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
            print('Login efetuado com sucesso!')
            return redirect('/cliente')
    context = {}
    return render(request, 'login.html', context = context)

#C1
def c1(request):
    context = {}
    return render(request, 'C1_templates/Comercial1_MainPage.html', context = context)

def c2(request):
    context = {}
    return render(request, 'C2_templates/Comercial2_MainPage.html', context = context)

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
        products = Product.objects.filter(ProductStatus='True')
        context = {'products': products}
        return render(request, 'C1_templates/ListarProdutos.html', context=context)

def listPrdt2(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'C2_templates/ListarProdutos.html', context=context)

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

def addSale2(request):
    if request.method == 'POST':
        # Handle form submission
        form = addSaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.save()
            product = Product.objects.get(ProductTypeId=sale.ProductTypeId)
            product.ProductPrice = product.ProductPrice * (1-(sale.Promotion/100))
            product.save()
            return redirect('/c2')
    else:
        # Handle GET request
        form = addSaleForm()
    return render(request, 'C2_templates/InserirPromocao.html', {'form': form})

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

def removeSale2(request):
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
            return redirect('/c2')
    else:
        # Handle GET request
        form = removeSaleForm()
    return render(request, 'C2_templates/RemoverPromocao.html', {'form': form})

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

def list_cliente(request):
    if request.method == 'GET':
        clients = database.list_client()
        context = {'clients': clients}
        return render(request, 'C1_templates/ListarClientes.html', context=context)

def deletePrdt(request,ProductId):
    prdt = get_object_or_404(Product, pk=ProductId)
    prdt.delete()    
    return redirect('/c1/listPrdt')

def list_orders(request):
    if request.method == 'GET':
        orders = database.list_orders()
        context = context = {'orders': orders}
        return render(request, 'C1_templates/ListarEncomendas.html', context=context)

def list_orders2(request):
    if request.method == 'GET':
        orders = database.list_orders()
        context = context = {'orders': orders}
        return render(request, 'C2_templates/ListarEncomendas.html', context=context)

#Adm + Parceiro
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

def gerirParc(request):
    if request.method == 'GET':
        products = database.funcao3()
        context = {'products': products}
        return render(request, 'Parc_templates/GerirProdutos.html', context=context)

def deleteprdParc(request, id):
    prod = get_object_or_404(Product,pk=id)
    prod.delete()
    return redirect('/par/gerirParc')

def editarproc(request, id):
    Prod = Product.objects.get(pk=id)
    form = editPrdtFormParc(request.POST or None,instance=Prod)
    if form.is_valid():
        form.save()
        return redirect('/par/gerirParc/')
    
    return render(request, 'Parc_templates/EditarProdutos.html', {'form': form})

def listxml(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=novosprod.xml'
    products =  Product.objects.filter(Q(ProductUserId='c1')&Q(ProductQuantity__lte=10))
    lines = []
    for prod in products:
        lines.append(f'<Product>\n\t<ID="{prod.ProductId}>\n\t<Name="{prod.ProductName}">\n\t<Quantity="20"/>\n</Product>\n' )
    response.writelines(lines)
    return response

def listpedirproc(request):
    if request.method == 'GET':
        products = database.funcao4()
        context = {'products': products}
        return render(request, 'Adm_templates/PedirProdList.html', context=context)

def listpedirproc2(request):
    if request.method == 'GET':
        products = database.funcao4()
        context = {'products': products}
        return render(request, 'C2_templates/PedirProdList.html', context=context)

def pedirproc(request):
    if request.method == 'GET':
        products = database.funcao4()
        context = {'products': products}
        return render(request, 'C1_templates/PedirProdList.html', context=context)

#Cliente

def client(request):
    if request.method == 'GET':
        products = Product.objects.order_by('ProductPrice')[:6]
        context = {'products': products}
    return render(request, 'Clients_templates/Client_main_page.html', context = context)

def categorias(request):
    context = {}
    return render(request, 'Clients_templates/Categorias.html', context = context)

def categorias2(request):
    context = {}
    return render(request, 'Categorias.html', context = context)

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

def playstation_list2(request):
    products = database.listjogosPS()
    context = {'products': products}
    return render(request,'PlayStation_list.html',context=context)

def xbox_list2(request):
    products = database.listjogosXbox()
    context = {'products': products}
    return render(request,'Xbox_list.html',context=context)

def pc_list2(request):
    products = database.listjogosPC()
    context = {'products': products}
    return render(request,'PC_list.html',context=context)

def nintendo_list2(request):
    products = database.listjogosNintendo()
    context = {'products': products}
    return render(request,'Nintendo_list.html',context=context)

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

def addCartUser(request,id):
    userid = request.session.get('id')
    prdId = id
    if Cart.objects.filter(Q(ProductId=prdId)).exists():
        cart = Cart.objects.get(Q(ProductId=prdId))
        if cart.ProductQuantity < Product.objects.get(pk=prdId).ProductQuantity:
            cart.ProductQuantity = cart.ProductQuantity + 1
            Product.objects.get(pk=prdId).ProductQuantity = Product.objects.get(pk=prdId).ProductQuantity - 1
        else:
            print('Não pode comprar mais do que o stock')
        cart.save()
    else:
        cart = Cart.objects.create(UserId=userid,ProductId=prdId,ProductQuantity=1,ProductTotalPrice=Product.objects.get(pk=prdId).ProductPrice)
    return redirect('/cliente')

def cart(request):
    userid = request.session.get('id')
    cart = Cart.objects.filter(UserId=userid)
    context = {'cart': cart}
    return render(request, 'Clients_templates/Cart.html', context=context)

def addCartNoUser(request,id):
    prdId = id
    if Cart.objects.filter(Q(ProductId=prdId)&Q(UserId=0)).exists():
        cart = Cart.objects.get(Q(ProductId=prdId))
        cart.ProductQuantity = cart.ProductQuantity + 1
        cart.save()
        print('existe')
    else:
        print('antes')
        cart = Cart.objects.create(UserId=0,ProductId=prdId,ProductQuantity=1,ProductTotalPrice=Product.objects.get(pk=prdId).ProductPrice)
        print('depois')
    return redirect('/')

def cartNoUser(request):
    cart = Cart.objects.filter(UserId=0)
    context = {'cart': cart}
    return render(request, 'Cart.html', context=context)
   
def finalizar(request):
    userid = request.session.get('id')
    totalprice = 0
    postgres = connections['second'].cursor()
    postgres.execute("CALL insertorder(%s,%s);",(userid,totalprice))
    #get quantatity of products
    cart = Cart.objects.filter(UserId=userid)

    for item in cart:
        prodid = item.ProductId
        quant = item.ProductQuantity
        price = item.ProductTotalPrice
        totalprice = totalprice + (quant * price)
        postgres.execute("CALL maxid(%s,%s,%s)",(prodid,quant,totalprice))
    
    connections['second'].commit()
    postgres.close()
    return redirect('/cliente')

def cartNoUserLogin(request):
    if request.method == 'POST':
        email = request.POST.get('UserEmail')
        password = request.POST.get('UserPassword')
        resultado = database.login(email, password)

        if resultado == resultado:
            request.session['id'] = resultado

            print('Login efetuado com sucesso!')


            return redirect('/cliente/cart')
    context = {}
    return render(request, 'login.html', context = context)

def orders_list(request):
    userid = request.session.get('id')
    print(userid)
    if request.method == 'GET':
        postgres = connections['second'].cursor()
        #call postgres view with an id
        postgres.execute("SELECT * FROM OrdersView WHERE UserId = %s", [userid])
    
        orders = postgres.fetchall()
        postgres.close()
        context = {'orders': orders}
    return render(request, 'Clients_templates/ListarEncomendas.html', context=context)

def list_orders_filter(request,data):
    postgres = connections['second'].cursor()
    #call postgres function with a date
    postgres.execute("SELECT * FROM total_encomendas(%s)",[data])
    orders = postgres.fetchall()
    postgres.close()
    context = {'orders': orders}
    return render(request, 'C1_templates/ListarEncomendas.html', context=context)

def list_orders_filter2(request,data):
    postgres = connections['second'].cursor()
    #call postgres function with a date
    postgres.execute("SELECT * FROM total_encomendas_entre_datas(%s)",[data])
    orders = postgres.fetchall()
    postgres.close()
    context = {'orders': orders}
    return render(request, 'C2_templates/ListarEncomendas.html', context=context)