from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
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
                return render(request,'register.html',{'message':"Username is Taken"})
            elif User.objects.filter(email=email).exists():
                print("Email is taken")
                return render(request,'register.html',{'message':"Email is Taken"})
            else:
                user  = User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                user.save()
                print('User Created!!!')
                return redirect('/')
        else:
            print("Password not match")
            return render(request,'register.html',{'message':"Password not match"})
    else:
        # this is for get request
        return render(request, 'register.html')