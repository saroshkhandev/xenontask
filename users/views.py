from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import contactus


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data = contactus(
                name = cd['name'],
                email = cd['email'],
                message = cd['message']
            )
            data.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {
        'form': form
    })

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
