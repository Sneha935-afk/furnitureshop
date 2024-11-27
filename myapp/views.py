from django.shortcuts import render, redirect
from myapp.models import CategoryDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from myapp.models import ProductDb

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from webapp.models import contactDb
from django.contrib import messages


# Create your views here.

def indexpage(request):
    cun=CategoryDb.objects.count()
    cu=ProductDb.objects.count()
    return render(request, "indexpage.html",{'cun':cun,'cu':cu})


def addcategory(request):
    return render(request, "addcategory.html")


def savecategory(request):
    if request.method == "POST":
        category = request.POST.get('categoryname')
        desc = request.POST.get('description')
        image = request.FILES['img']

        obj = CategoryDb(Categoryname=category, Description=desc, Categoryimage=image)
        obj.save()
        messages.success(request,"Category saved...")
        return redirect(addcategory)


def editcategory(request, stud_id):
    stud = CategoryDb.objects.get(id=stud_id)
    return render(request, "editcategory.html", {'stud': stud})


def displaycategory(request):
    data = CategoryDb.objects.all()
    return render(request, "displaycategory.html", {'data': data})


def updatecategory(request, stud_id):
    if request.method == "POST":
        category = request.POST.get('categoryname')
        desc = request.POST.get('description')
        try:
            im = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=stud_id).Categoryimage
        CategoryDb.objects.filter(id=stud_id).update(Categoryname=category, Description=desc, Categoryimage=file)
        messages.success(request,"updates sucessfully..")
        return redirect(displaycategory)


def deletecategory(request, stud_id):
    x = CategoryDb.objects.filter(id=stud_id)
    x.delete()

    messages.error(request,"category deleted...")
    return redirect(displaycategory)


def addproduct(request):
    data = CategoryDb.objects.all()
    return render(request, "addproduct.html", {'data': data})


def saveproduct(request):
    if request.method == "POST":
        productcategory = request.POST.get('productcategory')
        pname = request.POST.get('productname')
        Quantity = request.POST.get('Quantity')
        MRP = request.POST.get('MRP')
        desc = request.POST.get('description')
        country = request.POST.get('country of origin')
        manufacture = request.POST.get('manufactured')
        image = request.FILES['img']
        image1 = request.FILES['img1']
        image2 = request.FILES['img2']

        obj = ProductDb(Productcategory=productcategory, Productname=pname, Quantity=Quantity, MRP=MRP,
                        Description=desc, Countryorigin=country, Manufacturedby=manufacture, Productimage=image,
                        Productimage1=image1, Productimage2=image2)
        obj.save()
        messages.success(request, "Product saved...")
        return redirect(addproduct)


def editproduct(request, stud_id):
    data = CategoryDb.objects.all()
    stud = ProductDb.objects.get(id=stud_id)
    return render(request, "editproduct.html", {'stud': stud, 'data': data})


def displayproduct(request):
    data = ProductDb.objects.all()
    return render(request, "displayproduct.html", {'data': data})


def updateproduct(request, stud_id):
    if request.method == "POST":
        productcategory = request.POST.get('productcategory')
        pname = request.POST.get('productname')
        Quantity = request.POST.get('Quantity')
        MRP = request.POST.get('MRP')
        desc = request.POST.get('description')
        country = request.POST.get('country of origin')
        manufacture = request.POST.get('manufactured')

        try:
            im = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=stud_id).Productimage
        try:
            im1 = request.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(im1.name, im1)
        except MultiValueDictKeyError:
            file1 = ProductDb.objects.get(id=stud_id).Productimage1
        try:
            im2 = request.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(im2.name, im2)
        except MultiValueDictKeyError:
            file2 = ProductDb.objects.get(id=stud_id).Productimage2

        ProductDb.objects.filter(id=stud_id).update(Productcategory=productcategory, Productname=pname,
                                                    Quantity=Quantity, MRP=MRP, Description=desc, Countryorigin=country,
                                                    Manufacturedby=manufacture, Productimage=file, Productimage1=file1,
                                                    Productimage2=file2)
        messages.success(request,"update suceffuly...")
        return redirect(displayproduct)


def deleteproduct(request, stud_id):
    x = ProductDb.objects.filter(id=stud_id)
    x.delete()

    messages.error(request,"product delected...")
    return redirect(displayproduct)


def loginpage(request):
    return render(request, "login.html")


def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        psw = request.POST.get('password')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=psw)
            if user is not None:
                login(request, user)
                request.session['username']=un
                request.session['password']=psw
                messages.success(request,"welcome...!")

                return redirect(indexpage)
            else:
                messages.error(request,"please check your password...!")
                return redirect(loginpage)

        else:
            messages.warning(request,"invalid username....!")
            return redirect(loginpage)
    else:
        return redirect(loginpage)



def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"delected sucessfully...!")
    return redirect(loginpage)


def contactdata(request):
    con=contactDb.objects.all()
    return render(request,"contact_data.html",{'con':con})




