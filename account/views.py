from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def reg(request):
    if request.method == "GET":
        return render(request, 'account/reg.html', {})
    elif request.method == 'POST':
        # ...
        return render(request, 'account/reg_res.html', {})


def confirm(request):
    return render(request, 'account/confirm.html', {})


def entry(request):
    return render(request, 'account/entry.html', {})


def exit(request):
    return render(request, 'account/exit.html', {})


def profile(request):
    return render(request, 'account/profile.html', {})


def reset(request):
    return render(request, 'account/reset.html', {})
