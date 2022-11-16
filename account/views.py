from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from hashlib import md5


def reg(request):
    if request.method == "GET":
        return render(request, 'account/reg.html', {})
    elif request.method == 'POST':
        # 1. Отримати із форми реєстраціні данні
        login = request.POST.get('login')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')
        # 2. Сценарій реєстрації
        report = dict()
        passw = md5(pass1.encode('utf-8')).hexdigest()
        new_user = User.objects.create_user(login, email, passw)
        if new_user is None:
            report['msg'] ='У реєстрації відмовлено!'
        else:
            report['msg'] ='Ви успішно зареєстровані!'
        # 3. Завантажуємо звіт на сторінку результатів
        return render(request, 'account/reg_res.html', context=report)


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
