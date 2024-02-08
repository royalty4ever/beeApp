from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

# To logout and authenticate users
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages







# -------------------------- Home Page ---------------------------------
def index(request):
    return render(request, "beeApp/index.html")

# -------------------------- Bee Rules and Regulations ---------------------------------
def bee_rules(request):
    return render(request, "beeApp/bee_rules.html")


# -------------Creating Registration Page-------------------------------
def register(request):
    return render(request, "beeApp/register.html")


# -------------------------- GALLERY ---------------------------------
def gallery(request):
    return render(request, "beeApp/gallery.html")
 

# ----------------------- Register a User ------------------------------

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("login")
        
    context = { 'form':form }

    return render(request, 'beeApp/register.html', context=context)


# ----------------------- Login a User -----------------------------------
def login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            # To verify if the user exist

            if user is not None:

                auth.login(request, user)


                return redirect("dashboard")

    context = {'form':form}

    return render(request, "beeApp/login.html", context=context)

# ---------------------- Dashboard -----------------------------------

@login_required(login_url='login')

def dashboard(request): 

    contestants_records = Record.objects.all()

    context = { 'records': contestants_records } 

    return render(request, "beeApp/dashboard.html", context=context)


# -------------------------Create a record--------------------------------

@login_required(login_url='login')

def create_record(request): 

    form = CreateRecordForm()

    if request.method == "POST":
    
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your record was created successfully!")

            return redirect("dashboard")
    
    context = {'form':form}

    return render(request, 'beeApp/create_record.html', context=context)


# -------------------------Update a record--------------------------------

@login_required(login_url='login')

def update_record(request, pk): 

    reocrd = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=reocrd)

    if request.method == "POST":
    
        form = UpdateRecordForm(request.POST, instance=reocrd)

        if form.is_valid():
            form.save()

            messages.success(request, "Your record was updated successfully!")

            return redirect("dashboard")
    
    context = {'form':form}

    return render(request, 'beeApp/update_record.html', context=context)


# -------------------------Read /  View a singular record--------------------------------

@login_required(login_url='login')

def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'beeApp/view_record.html', context=context) 


# -------------------------Delete a record--------------------------------

@login_required(login_url='login')

def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted successfully!")

    return redirect("dashboard")

   

# ------------------------ User Logout ----------------------------------

def logout(request):
    
    auth.logout(request)

    messages.success(request, "You are logged out successfully!")

    return redirect("login")