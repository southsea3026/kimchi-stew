from django.shortcuts import render
from .models import StoryDb


def index(request):
    story_list = StoryDb.objects.order_by('-create_date')
    context = {'story_list': story_list}
    return render(request, 'kimchi/index.html', context)

def textplay(request):
    return render(request, 'kimchi/textplay.html')

def page_not_found(request, exception):
    return render(request, '404.html', {})