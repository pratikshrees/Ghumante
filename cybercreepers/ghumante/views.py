from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.



def abc(request):
    return render(request,'abc.html')

def registration(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same!") 
        
        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')
        
    return render(request,'registration.html') 

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass']
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect !!!")
        
    return render(request,'login.html')
        

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')   



 



def map(request):
    return render(request,'map.html')

def profile(request):
    return render(request,'profile.html')

def routes(request):
    return render(request,'routes.html')

def shop(request):
    return render(request,'shop.html')
