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
        f = open('utils/private_' + name + '.pem', 'wt')
        f.write(key.export_key(format='PEM'))
        f.close()

        print('**********************')
        print(key.export_key(format='PEM'))
        print('**********************')

        # Generate Public Key
        os.system("openssl ec -in utils/private_" + name + ".pem -pubout -out utils/public_" + name + ".pem")

        temp = open("utils/public_" + name + ".pem", "r")
        user_details_obj.public_key = temp.read()
        user_details_obj.save()
        # Delete private key after generating public key
        # try:
        #     os.remove('utils/private_' + name + '.pem')
        #     os.remove('utils/public_' + name + '.pem')
        # except Exception as e:
        #     pass
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
            if user.is_active:
                login(request, user)
                return redirect('/home')
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse("Invalid login")
    elif request.method == "GET":
        return render(request, 'welcome/login.html')


@login_required(login_url='/')
def user_logout(request):
    logout(request)
    return redirect('/')
