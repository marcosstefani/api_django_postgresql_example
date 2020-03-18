from django.urls import path

from . import views

urlpatterns = [
    path('letter/digit', views.letter_digit),
]
