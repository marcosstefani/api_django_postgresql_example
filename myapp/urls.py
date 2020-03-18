from django.urls import path

from . import views

urlpatterns = [
    path('birthdays', views.user_birthday),
    path('birthdays/sum', views.user_birthday_sum)
]
