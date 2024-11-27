from django.db import models

# Create your models here.

class contactDb(models.Model):
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=300,null=True,blank=True)



class singupDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    repeatpassword=models.CharField(max_length=100,null=True,blank=True)


class cartDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Productname=models.CharField(max_length=100,null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)
    Quantity=models.CharField(max_length=100,null=True,blank=True)
    product_image=models.ImageField(upload_to="Cart Images",null=True,blank=True)



class checkoutDb(models.Model):
    country=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    Companyname=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    emailaddress=models.CharField(max_length=100,null=True,blank=True)
    mobilenumber=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
    message=models.TextField(max_length=300,null=True,blank=True)

