from django.shortcuts import render
from .models import Person
from .forms import UserForm, SmsForm, UsersForm2, First_name
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .smsc_api import *  # точно нужно всё импортировать?
import uuid
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect


def my_random_string(string_length=10):
    """Возвращает случайную строку"""  # а зачем случайная строка?
    """Возвращает случайную строку, нужно для отправки кода смс"""
    random = str(uuid.uuid4())  # конвертирование UUID4 в строку.
    random = random.upper()
    random = random.replace("-", "")
    return random[0:string_length]


def registration(request):
    """
         Функция регистрации профиля персоны
         user_form -  работает из админки и содержит поле username пользвоателя
         sms_form -  Нужна для обработки кода смс
    """
    user_form = UserForm()
    sms_form = SmsForm()
    first_name_form = First_name()
    disabled, disabled2 = "", "disabled"  # Параметры кнопок,которые передаются в html

    if request.is_ajax():
        """
        Если запрос на бэкенд , это ajax запрос, 
        то бэкенд валидирует данные введйнные пользователем в форму телефона - user_form
        """
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            return JsonResponse({'s': True})
        else:
            return JsonResponse({'error': user_form.errors})

    if request.method == "POST" and 'code' in request.POST:

        user_form = UserForm(request.POST)

        if user_form.is_valid():
            #  Отправка сообщения и валидация номера
            smsc = SMSC()  # Иницилизация класса отправки смс стороннего сервиса
            phone = user_form.cleaned_data['username']  # Форма ввода телефона

            mes = (my_random_string(4))  # смс пароль
            print(mes)
            Sms_message = Person(id=1, sms_mes=mes)
            Sms_message.save()
            # counter = ['19', '1', '0.9', '194.4' ] #  Симуляция успешнйо отправки смс, для дэбага
            # d = [ '-1' ]
            counter = smsc.send_sms(phones=phone, message=mes, sender="me")  # Отправка смс с
            # введёными данными пользователя
            status_phone = smsc.get_status(phone=phone, id=counter[0])
            print(status_phone)

            if len(counter) < 3 and status_phone[0] != "-1":
                #  Проверка со стороны сервиса SMSC
                messages.error(request, "Такого номера нет в базе или Вы ошиблись при вводе номера")
            else:
                messages.success(request, "Код отправлен!")
                disabled = "disabled"
                disabled2 = ""

    if request.method == "POST" and 'reg' in request.POST:

        user_form = UserForm(request.POST)
        first_name_form = First_name(request.POST)
        sms_form = SmsForm(request.POST)
        if user_form.is_valid () and sms_form.is_valid() and first_name_form.is_valid():
            get_id_first_person = Person.objects.get(id=1)  # Получение пароля из смс
            # Проверка: совпадает ли код пользователя и код, отправленный ему
            if str(get_id_first_person.sms_mes) == sms_form.cleaned_data['sms_mes']:
                # создание или аутентификация персоны по введёным данным пользователя
                last_id = User.objects.latest('id').id
                last_i = Person.objects.latest('id').id
                password = "empty_password"
                first_nam = first_name_form.cleaned_data['first_name']
                # СОхранение номера телефона пользователя в модели
                phone = user_form.cleaned_data['username']

                User.objects.create_user(username = first_name_form.cleaned_data['first_name'],email=phone, id=int(last_id)+1, password=password)
                create_person = Person(users_id = last_id+1,phone=phone, id=last_i+1) # ПРисваивание id новому пользователю
                create_person.save()

                user = authenticate(
                    username=first_nam,
                    password=password
                )
                login(request, user)
                messages.success(request, "Вы успешно зарегистрированы!")
                return redirect('/')
            else:
                messages.error(request, "Код не подходит, Вы не ошиблись? Проверьте, пожалуйста")
                disabled2 = ""
    return render(request, 'sign_ip.html',
                   {"user_form": user_form,
                    "sms_form": sms_form,
                    "first_name":first_name_form,
                    "id": id,
                    "disabled": disabled,
                    "disabled2": disabled2})


def MyLoginView(request):
    """
         Функция авторизации
         user_form -  работает из админки и содержит поле username пользователя (номер телефона)
         Функция входа пользователя на сайт
         sms_form -  Нужна для обработки кода смс
    """
    user_form = UsersForm2()
    sms_form = SmsForm()
    first_name_form = First_name()
    disabled, disabled2 = "","disabled"

    if request.is_ajax():
        """
       Если запрос на бэкенд , это ajax запрос, 
       то бэкенд валидирует данные введйнные пользователем в форму телефона - user_form
       Так же после этого идёт проверка что такой пользователь существует       
       """
        user_form = UsersForm2(request.POST)
        if user_form.is_valid():
            if User.objects.filter(email=user_form.cleaned_data['username']).exists():
                return JsonResponse({'s': True})
            else:

                return JsonResponse({'error': {"username": "Этого номера еще нет, Вам нужно зарегистрироваться"}})
        else:
            return JsonResponse({'error': user_form.errors})

    if request.method == "POST" and 'code' in request.POST:
        user_form = UsersForm2(request.POST)
        if user_form.is_valid():
            # проверка существует ли пользователь с таким номером или нет
            if User.objects.filter(email=user_form.cleaned_data['username']).exists():
                # Отправка сообщения и валидация номера
                smsc = SMSC()  # Иницилизация класса отправки смс стороннего сервиса
                phone = user_form.cleaned_data[ 'username' ]  # Форма ввода телефона
                mes = my_random_string(4)  # смс пароль
                print(mes)
                Sms_message = Person(id=1, sms_mes=mes)  # Сохранения пароля в модель - sms_mes
                Sms_message.save()
                #counter = [ '19', '1', '0.9', '194.4' ]
                #d = [ '-1' ]
                # Отправка смс с введёными данными пользователя
                counter = smsc.send_sms(phones=phone, message=mes, sender="me")
                phone_status = smsc.get_status(phone=phone, id=counter[0])  # ПРоверка статуса отправки смс

                if len(counter) < 3 and phone_status[ 0 ] != "-1":
                    #  Проверка со стороны сервиса SMSC на валидность номера
                    messages.error(request, "Вы ввели неверный телефон!")
                else:
                    messages.success (request, "Код отправлен!")
                    disabled = "disabled"
                    disabled2 = ""
            else:
                messages.error (request, "Такого номера в базе не существует!")

    if request.method == "POST" and 'reg' in request.POST:

        user_form = UsersForm2(request.POST)
        sms_form = SmsForm (request.POST)
        first_name_form = First_name(request.POST)
        if user_form.is_valid () and sms_form.is_valid () and first_name_form.is_valid():
            password = "empty_password"
            # аутентификация пользователя
            firstname = first_name_form.cleaned_data['first_name']
            user = authenticate(
                username=firstname,
                password=password
            )
            if user is not None:
                # Проверка валидности пользователя
                get_id_first_person = Person.objects.get(id=1)
                # ПРоверка совпадает ли код отправленный персоне и код введенный пользователем в форме
                if str(get_id_first_person.sms_mes) == sms_form.cleaned_data['sms_mes']:
                    messages.success (request, "Вы успешно залогинили!")
                    # Перенаправление пользователя на его профиль
                    login(request, user)
                    current_user = request.user.personshop.id
                    return redirect('/')
                else:
                    messages.error(request, "Вы ввели неверный код!")
                disabled2 = ""

    return render (request, 'login.html',
                   {"user_form": user_form,
                    "sms_form": sms_form,
                    "first_name": first_name_form,
                    "id": id,
                    "disabled": disabled,
                    "disabled2":disabled2})




