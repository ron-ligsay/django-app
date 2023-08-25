from django.urls import path, include

from . import views

# URL Configuration (URLConf)
urlpatterns = [
    path('hello/', views.say_hello),
]