from django.urls import path
from webapp import views
urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/',views.productpage,name="productpage"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('productfilter/<cat_name>/',views.productfilter,name="productfilter"),
    path('singleproduct/<int:pro_id>/',views.singleproduct,name="singleproduct"),
    path('blogpage/',views.blogpage,name="blogpage"),
    path('singup/',views.singup,name="singup"),
    path('singin/',views.singin,name="singin"),
    path('savesingup/',views.savesingup,name="savesingup"),
    path('',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cart/',views.cart,name="cart"),
    path('deletecart/<int:d_id>/',views.deletecart,name="deletecart"),

    path('savecart/',views.savecart,name="savecart"),
    path('checkout/',views.checkout,name="checkout"),
    path('savecheckout/',views.savecheckout,name="savecheckout"),
    path('payment/',views.payment,name="payment"),

]