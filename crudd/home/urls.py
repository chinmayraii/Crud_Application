from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.uregs),
    path("ulogin",views.ulogin),
    path("webpage",views.webpage),
    path("addstudent",views.addstudent),
    path("delete",views.delete),
    path("del",views.delt),
    path("search",views.search),
    path("lgout",views.lgout),
    path("update",views.update)
]