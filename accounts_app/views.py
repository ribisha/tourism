from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['confirm_password']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save()
                print("Registration Completed Successfully")
        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('login_user')

    return render(request,'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login_user')

    return render(request,'login.html')

def logout_user(request):
    auth.logout(request)
    return redirect('/')
