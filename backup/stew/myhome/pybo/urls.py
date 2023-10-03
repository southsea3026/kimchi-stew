from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:StoryDb_id>/', views.text_play, name='textplay'),
    
   
]
