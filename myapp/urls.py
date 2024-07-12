from django.urls import path
from . import views
from .views import user_form, many_fields_form, add_user, upload_image


urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('show_orders/<int:days>', views.show_orders, name='show_orders'),
    path('user_form/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('user/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]