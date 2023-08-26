from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


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
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'Login First to view that page!')
        return redirect('home') 

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record Deleted Successfully!')
        return redirect('home')
    else:
        messages.success(request, 'Login First to view that page!')
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added Successfully!')
                return redirect('home')    
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'Login First to view that page!')
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        current_record = Record.objects.get(id=pk)
        # Create Form
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfully!')
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, 'Login First to view that page!')
        return redirect('home')