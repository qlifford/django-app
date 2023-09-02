from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f"Your account has been created with username: {username}, please login to continue!")
            return redirect('login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

@login_required()
def profile(request):
    return render(request, 'Users/profile.html', {})
