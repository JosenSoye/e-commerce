from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Q
from .models import *
from .form import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form =  UserRegisterForm(request.POST)
        if form.is_valid():
            a=form.save()
            profile.objects.create(user=a)
            # messages.success(request,'you have registered')
            return redirect(productpage)
    else:
        form= UserRegisterForm()
    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:  
            if user.is_superuser:  
                login(request, user)  
                return redirect(staffpage)  
            
            login(request, user)  
            return redirect(productpage)  
        else:
            messages.error(request, 'Invalid username or password')  
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect(productpage)


def staffpage(req):
    return render(req,'staffpage.html')

def addproduct(req):
    if req.method == 'POST':
        form=bookform(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect(staffpage)
    else:
        form=bookform()
    return render(req,'addproduct.html',{'form':form})

def editpage(req):
    product = Books.objects.all()
    return render(req,'alllist.html',{'products':product})

def edit(req,id):
    item=Books.objects.get(id=id)
    if req.method=='POST':
        form=bookform(req.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect(editpage)
    else:
        form=bookform(instance=item)
    return render(req,'edit.html',{'form':form})

def productpage(req):
    products = Books.objects.all()
    return render(req,'productpage.html',{'products':products})

def search(req):
    value= req.GET.get('search')
    if value:
        #pro=product1.objects.filter(pname__icontains=value)
        products=Books.objects.filter(
            Q (book_title__icontains=value) | Q (author__icontains=value))
    else:
        products=Books.objects.all()
    return render(req,'searchpage.html',{'products':products})

def detailpage(req,id):
    product=Books.objects.get(id=id)
    return render(req,'detailpage.html',{'det':product})

def paymentpage(req):
    return render(req,'payment.html')

def confirmationpage(req):
    return render(req,'confirmation.html')
