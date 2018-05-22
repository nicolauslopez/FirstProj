from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('polls:index')
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {'form': form}, )


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid() and user is not None:
            login(request, user)
            return redirect('polls:index')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form}, )