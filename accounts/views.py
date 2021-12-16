from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now Loggid in ")
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login Credentials ')
            return redirect('login')
        
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
      
        if password == confirm_password:
        
            if User.objects.filter(username=username).exists():        
                messages.error(request, 'Username Already Exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already Exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now LoggidIn')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, "You Are Registered Successfully")
                    return redirect('login')
          
      
        else:
            messages.error(request, 'Password Do Not Match')
            return redirect('register')
          
    else:
        return render(request, 'accounts/register.html')


def dashboard(request):
  return render(request, 'accounts/dashboard.html')


def logout(request):
  return redirect('home')