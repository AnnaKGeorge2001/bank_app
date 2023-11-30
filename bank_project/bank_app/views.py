from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from bank_app.forms import CustomerForm
from bank_app.models import Customer, Branch


# Create your views here.
def home(request):
    return render(request, 'home.html')


def new_page(request):
    return render(request, 'new_page.html')


def form_view(request):
    form = CustomerForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted!')

    return render(request, 'form.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        cpassword = request.POST.get('cpassword', '')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password is not matching")
            return redirect('register')
    return render(request, "register.html")
