from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignupUserForm, LoginUserForm, ProfileForm


login_template = 'users/login.html'
signup_template = 'users/signup.html'
profile_template = 'users/profile.html'


def login_user(request):
    print(request.POST)
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Authenticate
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('products:index')
            else:
                return render(request, login_template, { 'form' : form })
        else:
            return render(request, login_template, { 'form' : form })
    else:
        form = LoginUserForm()
        return render(request, login_template, { 'form' : form })
    

def signup_user(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            user = form.instance
            login(request, user)
            return redirect('products:index')
        else:
            return render(request, signup_template, { 'form' : form })
    else:
        form = SignupUserForm()
        return render(request, signup_template, { 'form' : form })
    
    
def logout_user(request):
    logout(request)
    return redirect('products:index')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, profile_template, { 'form' : form })
        else:
            print(form.errors)
            return render(request, profile_template, { 'form' : form })
    else:
        form = ProfileForm(instance=request.user)
        context = {
            'form' : form,
        }
        return render(request, profile_template, context)