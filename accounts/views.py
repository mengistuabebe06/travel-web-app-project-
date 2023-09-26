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
        user  = User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
        user.save()
        print('User Created!!!')
        return redirect('/')
    else:
        # this is for get request
        return render(request, 'register.html')