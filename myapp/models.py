from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    Categoryname=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Categoryimage=models.ImageField(upload_to="category",null=True,blank=True)


class ProductDb(models.Model):
    Productcategory=models.CharField(max_length=100,null=True,blank=True)
    Productname=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    MRP=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=300,null=True,blank=True)
    Countryorigin=models.CharField(max_length=100,null=True,blank=True)
    Manufacturedby=models.CharField(max_length=100,null=True,blank=True)
    Productimage=models.ImageField(upload_to="Product",null=True,blank=True)
    Productimage1=models.ImageField(upload_to="Product",null=True,blank=True)
    Productimage2=models.ImageField(upload_to="Product",null=True,blank=True)
