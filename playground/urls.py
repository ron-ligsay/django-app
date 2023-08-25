import debug_toolbar
from django.urls import path, include
from . import views

# URL Configuration (URLConf)
urlpatterns = [
    path('hello/',views.say_hello),
    path('playground/', include('playground.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]