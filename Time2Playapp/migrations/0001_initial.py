# Generated by Django 4.1.3 on 2023-01-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('CartId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('ProductId', models.IntegerField()),
                ('ProductQuantity', models.IntegerField()),
                ('ProductTotalPrice', models.FloatField()),
                ('CartStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('InvoiceId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('InvoiceDate', models.DateTimeField()),
                ('InvoiceTotalPrice', models.FloatField()),
                ('InvoiceOrderId', models.IntegerField()),
                ('InvoiceAddress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item_Order',
            fields=[
                ('Item_OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('OrderId', models.IntegerField()),
                ('ProductId', models.IntegerField()),
                ('ProductQuantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('UserId', models.IntegerField()),
                ('OrderDate', models.DateTimeField()),
                ('OrderStatus', models.TextField(default='Em espera', max_length=100)),
                ('OrderTotalPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=100)),
                ('ProductDescription', models.CharField(max_length=100)),
                ('ProductPrice', models.FloatField()),
                ('ProductQuantity', models.IntegerField()),
                ('ProductImage', models.ImageField(upload_to='static/images/')),
                ('ProductTypeId', models.CharField(max_length=100)),
                ('ProductStatus', models.BooleanField(default=True)),
                ('ProductUserId', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('ProductTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductTypeName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('SalesId', models.AutoField(primary_key=True, serialize=False)),
                ('ProductTypeId', models.CharField(max_length=100)),
                ('Promotion', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(max_length=100)),
                ('UserEmail', models.EmailField(max_length=100)),
                ('UserPassword', models.CharField(max_length=100)),
                ('UserType', models.CharField(max_length=100)),
                ('UserStatus', models.BooleanField(default=False)),
            ],
        ),
    ]
