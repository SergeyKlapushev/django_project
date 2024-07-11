import datetime

from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta
from django.shortcuts import render


# Create your views here.


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