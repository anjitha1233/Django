from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def form(request):
    return render(request, 'form.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']

        password=request.POST['password']
        user=auth.authenticate(username=username , password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,'invalid credential')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken')
                return redirect('register')

            else:
                 user = User.objects.create_user(username=username, password=password)
                 user.save
                 print("user created")
                 return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def submitform(request):
    if request.method == 'POST':


        messages.info(request, 'Application Accepted')
        return render(request, 'form2.html')
    else:
        return redirect('/')
    return redirect('formapply')
def formapply(request):
    return render(request,'form2.html')