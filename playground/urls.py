from django.urls import path
from . import views

# URL Configuration (URLConf)
urlpatterns = [
    path('hello/',views.say_hello)
]