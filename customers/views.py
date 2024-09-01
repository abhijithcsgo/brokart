from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Customer
# Create your views here.

def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # creates user account
            user = User.objects.create_user(
                username =username,
                password = password,
                email = email
            )
            # create customer accout
            customer = Customer.objects.create(
                user = user,
                address = address,
                phone = phone
            )
            # return redirect('home')
            success_message = "User registred succesfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message = "Duplicate username or invalide inputs"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password) 
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid user credentials")
    return render(request,'account.html',context)


def signout(request):
    logout(request)
    return redirect('home')
    