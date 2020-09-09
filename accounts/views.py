from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name= request.POST['firstname']
        last_name= request.POST['lastname']
        phone= request.POST['phone']
        password1= request.POST['passwordreg']
        password2= request.POST['passwordreg2']
        email= request.POST['emailreg']
        username = email

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already exists')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user creaed')
                return redirect('login')
    else:
            return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['email']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
    else:
        messages.info(request,"invalid credentials")
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect("/")