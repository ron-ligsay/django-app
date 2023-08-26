from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

# def login_user(request):
#     pass

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save user to database
            form.save()
            # get username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # or
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # authenticate user then login
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
    else:
        form = SignUpForm()    
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


# Create your views here.
def home(request):
    # check to see if logging in
    if request.method == 'POST':
        # attempt to authenticate user
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        # user = authenticate(
        #     request,
        #     username=request.POST['username'],
        #     password=request.POST['password']
        # )
        if user is not None:
            # login user
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.success(request, 'Error logging in - please try again...')
            return redirect('home')
    else:
        return render(request, 'home.html', {})



