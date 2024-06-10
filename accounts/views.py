from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import RegistrationForm
from .models import Account
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('admin:index')
        else:
            messages.warning(request, 'Invalid login credentials')
            return redirect('login')
    
    return render(request, 'layouts/accounts/login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = email.split("@")[0]
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password
            )
            user.phone_number = phone_number
            user.save()
            return redirect('home')
    else:
        form = RegistrationForm()
    
    context = {
        'form': form
    }

    return render(request, 'layouts/accounts/register.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')