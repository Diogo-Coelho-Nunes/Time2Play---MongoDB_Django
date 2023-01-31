from django.db import models

# Create your models here.
#MongoDB Tabels
#User model
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    UserEmail = models.EmailField(max_length=100)
    UserPassword = models.CharField(max_length=100)
    UserType = models.CharField(max_length=100) #Admin, C1, C2, Parceiro, Cliente
    UserStatus = models.CharField(max_length=100,default='False') #Ativo, Inativo, Bloqueado

#ProductsType model
class ProductType(models.Model):
    ProductTypeId = models.AutoField(primary_key=True)
    ProductTypeName = models.CharField(max_length=100)

#Products model
class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100)
    ProductDescription = models.CharField(max_length=100)
    ProductPrice = models.FloatField()
    ProductQuantity = models.IntegerField()
    ProductImage = models.ImageField(null=True,blank=True,upload_to="images/")
    ProductTypeId = models.IntegerField()
    ProductStatus = models.CharField(max_length=100,default='False') # #Ativo, Inativo, Fica "False" se o gestor enetender que não é um bom produto para venda
    ProductUserId = models.TextField() #Id do utilizador que adicionou o produto: c1, parceiro

#Sales model
class Sales(models.Model):
    SalesId = models.AutoField(primary_key=True)
    ProductTypeId = models.IntegerField()
    Promotion = models.FloatField()
    
#Cart model
class Cart(models.Model):
    CartId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    ProductId = models.IntegerField()
    ProductQuantity = models.IntegerField()
    ProductTotalPrice = models.FloatField()
    CartStatus = models.BooleanField(default=False) #Passa a True depois de selecionar "comprar" os produtos, estes saem do carrinho e lança-se uma fatura