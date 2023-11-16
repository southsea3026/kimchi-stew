from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import textStory

def index(request):
    request.session['min_id'] = 1
    request.session['score'] = 0
    next_text = textStory.objects.order_by('id').first()
    request.session['min_id'] = 1
    
    story_list = textStory.objects.order_by('-create_date')
    context = {'story_list': story_list}
    return render(request, 'kimchi/index.html', context)

def textplay(request, reset=False):
    min_id = request.session.get('min_id', 1)
    next_text = textStory.objects.filter(id__gt=min_id).order_by('id').first()
    if next_text:
        request.session['min_id'] = next_text.id

    context = {'next_text': next_text}
    return render(request, 'kimchi/textplay.html', context)

def reset(request, reset=False):
    return render(requset, 'kimchi/index.html')
        
def increase_score(request, score_increment):
    score = request.session.get('score', 0)
    score += int(score_increment)
    request.session['score'] = score
    return redirect('kimchi:textplay')

def end(requset):
    return render(requset, 'kimchi/end.html')