from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successful...!")
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials, Try Again...")
        return redirect('home')
    else:
        return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})