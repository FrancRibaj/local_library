from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import render ,  redirect
from django.contrib.auth import login, authenticate
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'registration/signup.html', context)
