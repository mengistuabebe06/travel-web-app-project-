from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# from .models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pass']
        conPass = request.POST['conpass']
        if password1 == conPass:
            if User.objects.filter(username=username).exists():
                print("Username is Taken")
                messages.info(request,"Username is Taken")
                return redirect('register')
                # return render(request,'register.html',{'message':"Username is Taken"})
            elif User.objects.filter(email=email).exists():
                print("Email is taken")
                messages.info(request,"Email is taken")
                return redirect('register')
                # return render(request,'register.html',{'message':"Email is Taken"})
            else:
                user  = User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                user.save()
                print('User Created!!!')
                messages.info(request,"User Created!!!")
                return redirect('login.html')
        else:
            print("Password not match")
            messages.info(request,"Password not match")
            return redirect('register')
            # return render(request,'register.html',{'message':"Password not match"})
    else:
        # this is for get request
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        # validateing the user input data with database user 
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Cerdintials")
            return redirect('login')
            # User is authenticated
        # if User.objects.filter(username=username).exists():
        #     if User.objects.filter(password=password).exists():
        #         redirect('/')
        #     else:
        #         print("password not match")
        # else:
        #     print("username is not exits")
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')