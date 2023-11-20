from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import render, redirect, get_object_or_404
app_name='bankapp'
def home(request):
    return render(request,'index.html')
# def formapply(request):
#     return render(request,'form2.html')
# def submitform(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         user = User.objects.create_user(username=username,email=email)
#         user.save
#         messages.info(request, 'Application Accepted')
#         return render(request, 'form2.html')
#     else:
#         return redirect('/')
#     return redirect('formapply')
