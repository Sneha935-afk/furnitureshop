from django.shortcuts import render,redirect
from myapp.models import ProductDb
from webapp.models import contactDb
from myapp.models import CategoryDb
from webapp.models import singupDb
from webapp.models import cartDb
from django.contrib import messages
from webapp.models import checkoutDb
import razorpay


# Create your views here.

def homepage(request):
    cat=CategoryDb.objects.all()
    c = cartDb.objects.filter(Username=request.session['name'])
    x = c.count

    return render(request,"home.html",{'cat':cat,'x':x})

def productpage(request):
    pro=ProductDb.objects.all()
    c = cartDb.objects.filter(Username=request.session['name'])
    x = c.count
    return render(request,"product.html",{'pro':pro,'x':x})

def about(request):
    c = cartDb.objects.filter(Username=request.session['name'])
    x = c.count
    return render(request,"about.html",{'x':x})

def contact(request):
    c = cartDb.objects.filter(Username=request.session['name'])
    x = c.count
    return render(request,"contact.html",{'x':x})



def savecontact(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        msg=request.POST.get('message')

        obj=contactDb(firstname=fname,lastname=lname,email=email,message=msg)

        obj.save()
        return redirect(contact)





def productfilter(request,cat_name):
    data=ProductDb.objects.filter(Productcategory=cat_name)
    return render(request,"productfilter.html",{'data':data})


def singleproduct(request,pro_id):
    data=ProductDb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data})

def blogpage(request):
    c = cartDb.objects.filter(Username=request.session['name'])
    x = c.count
    return render(request,"blog.html",{'x':x})


def singup(request):
    return render(request,"singup.html")

def singin(request):


    return render(request,"singin.html")


def savesingup(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        repass=request.POST.get('re_pass')

        obj = singupDb(name=name, email=email, password=password, repeatpassword=repass)
        if singupDb.objects.filter(name=name).exists():
            messages.warning(request,"user already exists...!")
            return  redirect(singup)
        elif singupDb.objects.filter(email=email).exists():
            messages.warning(request,"user already exists..!")
            return redirect(singup)
        obj.save()
        messages.success(request,"sucessfully completed..!")
        return redirect(singup)


def userlogin(request):
    if request.method == "POST":
        un=request.POST.get('your_name')
        pwd=request.POST.get('your_pass')

        if singupDb.objects.filter(name=un,password=pwd).exists():
            request.session['name']=un
            request.session['password']=pwd
            return redirect(homepage)
        else:
            return redirect(singin)

    else:
        return redirect(singin)


def userlogout(request):
    del request.session['name']
    del request.session['password']

    return redirect(homepage)


def savecart(request):
    if request.method == "POST":
        uname=request.POST.get('username')
        pname=request.POST.get('productname')
        qty=request.POST.get('quantity')
        total=request.POST.get('totalprice')

        try:
            file=ProductDb.objects.get(Productname=pname)
            img=file.Productimage
        except ProductDb.DoesNotExist:
            img=None




        obj=cartDb(Username=uname,Productname=pname,Total=total,Quantity=qty,Productimage=img)
        obj.save()
        return redirect(homepage)

def cart(request):
    c=cartDb.objects.filter(Username=request.session['name'])
    subtotal = 0
    shipping_amount = 0
    total = 0

    for i in c:
        subtotal = subtotal+i.Total
        if subtotal>50000:
            shipping_amount = 100
        else:
            shipping_amount = 250
        total = shipping_amount+subtotal
    return render(request,"cart.html",{'c':c,'subtotal':subtotal,'shipping_amount':shipping_amount,'total':total})
def deletecart(request,d_id):
    x=cartDb.objects.filter(id=d_id)
    x.delete()
    return redirect(cart)


def checkout(request):
    ca=cartDb.objects.filter(Username=request.session['name'])
    subtotal = 0
    shipping_amount = 0
    total = 0

    for i in ca:
        subtotal = subtotal+i.Total
        if subtotal>50000:
            shipping_amount = 100
        else:
            shipping_amount = 250
        total = shipping_amount+subtotal


    return render(request,"checkout.html",{'ca':ca,'subtotal':subtotal,'shipping_amount':shipping_amount,'total':total})

def savecheckout(request):
    if request.method == "POST":
        ctry = request.POST.get('cname')
        name = request.POST.get('name')
        cname = request.POST.get('companyname')
        addr = request.POST.get('address')
        mail = request.POST.get('emailaddress')
        phone = request.POST.get('phone')
        total = request.POST.get('totalprice')
        msg = request.POST.get('messages')

        obj=checkoutDb(country=ctry,name=name,Companyname=cname,emailaddress=mail,mobilenumber=phone,Totalprice=total,message=msg, address=addr)
        obj.save()
        return redirect(checkout)


def payment(request):
    customer = checkoutDb.objects.order_by('-id').first()

    pay = customer.Totalprice

    amount = int(pay*100)

    pay_str =str(amount)


    for i in pay_str:
        print(i)

    if request.method=="POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_uDRa6GNKP18CVi','joAqhW4gwZP2OtjyX1UVhgOq'))
        payment = client.order.create({'currency':order_currency,'amount':amount})
    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})