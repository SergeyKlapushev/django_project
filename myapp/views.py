import datetime

from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta
from django.shortcuts import render

import logging

from .forms import UserForm, ManyFieldsFormWidget
from .models import User
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm


# Create your views here.
logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form':form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp/many_fields_form.html',{'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp/user_form.html', {'form':form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form':form})


def index(request):
    return HttpResponse("Hi!")


def about_me(request):
    return HttpResponse("I'm Sergei")


def show_orders(request, days):
    now = datetime.date.today()
    start_date = now - datetime.timedelta(days=days)

    orders = {
        "tovar1": datetime.datetime(2024, 7, 2),
        "tovar2": datetime.datetime(2024, 6, 2),
        "tovar3": datetime.datetime(2023, 7, 2)
    }

    filtered_orders = {k: v for k, v in orders.items() if v.date() >= start_date}

    return render(request, 'myapp/show_orders.html', {'orders': filtered_orders, 'days': days})