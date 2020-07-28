from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# from .models import CreateUserForm
# Create your views here.
def home(request):
    return render(request,'basic.html')
def registerPage(request):
    
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f' Account created for {username}!')
            return redirect('login_url')
    else:
        form = UserRegisterForm()
    return render(request,'home/register.html',{'form':form})

def login(request):
    return render(request,'home/login.html')
@login_required
def profile(request):
    return render(request,'home/profile.html')


