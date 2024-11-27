from django.urls import path
from myapp import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('editcategory/<int:stud_id>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:stud_id>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:stud_id>/', views.deletecategory, name="deletecategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('displayproduct/', views.displayproduct, name="displayproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('editproduct/<int:stud_id>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:stud_id>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:stud_id>/', views.deleteproduct, name="deleteproduct"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('contactdata/', views.contactdata, name="contactdata"),


]
