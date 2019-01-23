# from __future__ import unicode_literals
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from . forms import AuthenticationForm

def signup(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signup.html', {'form': form})
