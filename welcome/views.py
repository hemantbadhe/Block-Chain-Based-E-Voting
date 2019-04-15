import subprocess

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Crypto.PublicKey import ECC

from simulation.models import UserDetail
import os


@login_required(login_url='/')
def home(request):
    context = {
        'tx': settings.N_TRANSACTIONS,
        'bl': settings.N_BLOCKS,
    }
    return render(request, 'welcome/home.html', context)


def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.create(first_name=first_name, last_name=last_name, username=email, email=email)
        user_obj.set_password(password)
        user_obj.save()

        user_details_obj = UserDetail.objects.create(user=user_obj)

        # Generate Private key
        name = "{}_{}".format(user_obj.first_name, user_obj.last_name)
        key = ECC.generate(curve='P-256')
        private_key = key.export_key(format='PEM')

        print('**********************')
        print(private_key)
        print('**********************')

        # Generate Public Key

        f = open('utils/public_' + name + '.pem', 'wt')
        f.write(key.public_key().export_key(format='PEM'))
        f.close()

        user_details_obj.public_key = key.public_key().export_key(format='PEM')
        user_details_obj.save()

        messages.success(request, 'User Sign Up success..!')
        return redirect('/')

    elif request.method == "GET":
        return render(request, 'welcome/sign_up.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.warning(request, "Invalid login")
            return render(request, 'welcome/login.html')
    elif request.method == "GET":
        return render(request, 'welcome/login.html')


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('/')
