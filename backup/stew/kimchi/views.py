from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import textStory

def page_not_found(request, exception):
    return render(request, '404.html', {})

def index(request):
    if not request.session.get('visited', False):
        request.session['visited'] = True
        request.session['current_story_index'] = 0
        request.session['score'] = 0

    story_list = textStory.objects.order_by('-create_date')
    context = {'story_list': story_list}
    return render(request, 'kimchi/index.html', context)

def textplay(request):

    if request.method == 'POST':
        choice = request.POST.get('choice')
        current_story_index = request.session.get('current_story_index', 0)
        score = request.session.get('score', 0)

        if choice == 'A':
            score += 1
        elif choice == 'B':
            score -= 1

        stories = textStory.objects.all()

        if current_story_index < len(stories) - 1:
            current_story_index += 1
        else:
            current_story_index = len(stories)
            current_story = "모든 스토리가 종료 되었습니다."
        request.session['current_story_index'] = current_story_index
        request.session['score'] = score

        return redirect('kimchi:textplay')

    stories = textStory.objects.all()
    current_story_index = request.session.get('current_story_index', 0)
    score = request.session.get('score', 0)

    if current_story_index < len(stories):
        current_story = stories[current_story_index]
    else:
        current_story = "모든 스토리가 종료되었습니다."

    return render(request, 'kimchi/textplay.html', {'current_story': current_story, 'score': score})
