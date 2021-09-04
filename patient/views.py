from django.shortcuts import redirect, render
from django.contrib import messages

from django.contrib.auth.models import Group
from .forms import CreateUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'patient-home.html')


def signup(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='patient')
            user.groups.add(group)

            username = form.cleaned_data.get('username')
            messages.success(
                request, 'Account created successfully for ' + username)

    context = {"form": form}
    return render(request, 'signup.html', context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.groups.all()[0].name == 'patient':
                return redirect('patient_home')
            else:
                return redirect('doct_home')
        else:
            messages.info(request, "Username or password is incorrect")
            return redirect('login')

    context = {}

    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
