from django.shortcuts import render,redirect
from .models import student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.hashers import check_password,make_password
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q


def uregs(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        if User.objects.filter(username=uname).exists():
            messages.info(request,"Username already exists")
            return render(request,'temp/uregs.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already exists")
            return render(request,'temp/uregs.html')   
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
            user.save()
            messages.success(request,"Successfully Registered")
            return render(request,'temp/ulogin.html')
    else:
        return render(request,'temp/uregs.html')
# def ulogin(request):
#     if request.method=='POST':
#       uname=request.POST['uname']
#       pwd=request.POST['pwd']
#       user=auth.authentication(username=uname,password=pwd)
#       if user is not None:
#         auth.login(request,user)
#         return render(request,'temp/webpage.html')
#       else:
#         messages.info(request,'Invalid User Id & Password')
#         return render(request,'temp/ulogin.html')
#     else:        
#         return render(request,'temp/ulogin.html')
def ulogin(request):
#  if not request.user.is_authenticated:
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['pwd']
        user = authenticate(username=uname, password=upass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully !!')
            st=student.objects.all()
            return render(request,'temp/webpage.html',{'st':st})
        else:
            return render(request, ("temp/ulogin.html"))
    else:
        return render(request, ("temp/ulogin.html"))        
                        
def lgout(request):
    auth.logout(request)
    messages.info(request,'sucessfully logout ')
    return render(request,'temp/uregs.html')

def webpage(request):
    st=student.objects.all()
    return render(request,'temp/webpage.html',{'st':st})
def addstudent(request):
    s=student() 
    s.fname=request.POST['fname']
    s.lname=request.POST['lname']
    s.cname=request.POST['cname']
    s.email=request.POST['email']
    pnumber=request.POST['pnumber']    
    s.pnumber=int(pnumber)
    s.save()
    st=student.objects.all()
    return render(request,('temp/webpage.html',{'st':st}))
def update(request):
    s=student()
    s.id=request.POST['sid']
    s.fname=request.POST['fname']
    s.lname=request.POST['lname']
    s.cname=request.POST['cname']
    s.email=request.POST['email']
    pnumber=request.POST['pnumber']    
    s.pnumber=int(pnumber)
    s.save()
    st=student.objects.all()
    return render(request,('temp/webpage.html',{'st':st}))
def delt(request):
    sid=request.GET['sid']
    student.objects.get(id=sid).delete()
    st=student.objects.all()
    return render(request,"temp/webpage.html",{'st':st}) 

def delete(request):
    # st=student.objects.all()
    return render(request,"temp/webpage.html") 

def search(request):
    find=request.POST['name']
    st=student.objects.filter(Q(fname=find) | Q(email=find)).all()
    return render(request,'temp/webpage.html',{'st':st})    
    # else:
    #     return render(request,('webpage.html'))         