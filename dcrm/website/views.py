from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Welcome, Registered Successfully ")
            return redirect('home')
        
    else:
        form = SignUpForm()

        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})