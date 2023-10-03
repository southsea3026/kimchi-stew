from django.shortcuts import render, get_object_or_404
from .models import StoryDb


def index(request):
    St = StoryDb.objects.order_by('-create_date')
    context = {'St': St}
    return render(request, 'start.html', context)

def text_play(request, StoryDb_id):
    s = StoryDb.objects.get(id=StoryDb_id)
    context = {'s': s}
    return render(request, 'text-play.html', context)



# Create your views here.