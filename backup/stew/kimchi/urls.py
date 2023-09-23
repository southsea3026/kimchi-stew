from django.urls import path

from . import views

app_name = 'kimchi'

urlpatterns = [
    path('', views.index, name='index'),
    path('textplay.html', views.textplay, name='textplay'),
]
