from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('show_orders/<int:days>', views.show_orders, name='show_orders'),
]