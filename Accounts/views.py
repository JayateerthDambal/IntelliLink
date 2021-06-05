from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# User Views


@login_required(login_url=('/login'))
def home(request):
    return render(request, 'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('/', {'user_name': username})
        else:
            messages.info(request, 'Username/ Password Incorrect!')

    return render(request, 'accounts/login.html')

##Signup Function/View
def signup_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account Created Succesfully for ' + user)
            form.save()
            return redirect('/login')
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')

