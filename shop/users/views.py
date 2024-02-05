from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


login_template = 'users/login.html'
signup_template = 'users/signup.html'

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products:index')
        else:
            error = 'Username or password is incorrect!'
            return render(request, login_template, { 'error' : error })
    else:
        return render(request, login_template)
    

def signup_user(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, signup_template)
    
    
def logout_user(request):
    logout(request)
    return redirect('products:index')