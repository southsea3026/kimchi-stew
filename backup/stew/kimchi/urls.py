from django.urls import path

from . import views

app_name = 'kimchi'

urlpatterns = [
    path('', views.index, name='index'),
    path('textplay', views.textplay, name='textplay'),
    path('textplay/reset/', views.textplay, {'reset': True}, name='textplay_reset'),
    path('increase_score/<int:score_increment>/', views.increase_score, name='increase_score'),
]
