from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail


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
        new_user = User.objects.create_user(login, email, pass1)
        if new_user is None:
            report['msg'] ='У реєстрації відмовлено!'
        else:
            # 3. Готуємо поштове повідомлення для підтвердження реєстрації
            url = f'http://127.0.0.1:8000/account/confirm?email={email}'
            subject = 'Підтвердження реєстрації на сайті Univer'
            body = f"""
                <hr/>
                <h3>Для підтвердження реєстрації перейдіть за посиланням:</h3>
                <div>
                    <a href="{url}">{url}</a>
                </div>
                <hr/>
            """
            # 4. Відправляємо повідомлення
            success = send_mail(subject, '', 'Site Univer', [email], fail_silently=False, html_message=body)
            if not success:
                report['info'] = 'Ваша пошта недійсна!'
            else:
                report['msg'] ='Ви успішно зареєстровані!'
                report['info'] = f'На вказаний Вами при реєстрації Email: {email}<br>відправлено повідомлення для її підтвердження'

        # !. Завантажуємо звіт на сторінку результатів
        return render(request, 'account/reg_res.html', context=report)


def confirm(request):
    # Зчитуємо пошту від якого прийшло підтвердження
    email = request.GET.get('email')

    # Знаходимо користуваяв із даним email
    user = User.objects.filter(email=email)

    # Додаємо користувача користувача до групи ConfirmedUser
    group = User.groups.filter(name='ConfirmedUser')
    User.groups.add(group)

    return render(request, 'account/confirm.html')


def entry(request):
    if request.method == "GET":
        return render(request, 'account/entry.html', {})
    elif request.method == 'POST':
        # 1. Отримати із форми данні авторизації
        _login = request.POST.get('login')
        _pass1 = request.POST.get('pass1')

        # 2. Сценарій авторизації
        report = dict()
        check_user = authenticate(request, username=_login, password=_pass1)
        if check_user is None:
            report['msg'] ='Користувач на знайдений!'
        else:
            report['msg'] ='Ви успішно авторизовані!'
            login(request, check_user)
        # !. Завантажуємо звіт на сторінку результатів
        return render(request, 'account/entry_res.html', context=report)


def exit(request):
    logout(request)
    return redirect('/home')


def profile(request):
    return render(request, 'account/profile.html', {})


def reset(request):
    return render(request, 'account/reset.html', {})
