
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

# Create your views here.


def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    #Django는 디폴트로 모든 Django 모델 클래스에 대해 "objects" 라는 Manager (django.db.models.Manager) 객체를 자동으로 추가한다 (이 objects라는 이름을 변경할 수도 있지만, 대부분 그대로 사용한다).
    #Django 에서 제공하는 이 Manager를 통해 특정 데이타를 필터링 할 수도 있고 정렬할 수도 있으며 기타 여러 기능들을 사용할 수 있다. 
    #order_by() 안에는 정렬 키를 나열할수 있는데 -가 붙으면 내림차순
    #ex. rows = Feedback.objects.order_by('id','-createData')
    '''
    template = loader.get_template('home/index.html')
    #loader.get_template('경로') 를
    '''
    context = {
        'lastest_question_list' : lastest_question_list,
    } 

    '''   
    return HttpResponse(template.render(context, request))
    '''

    return render(request, 'home/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #pk : primary key
    return render(request, 'home/detail.html', {'question': question})

def results(request, question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'home/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('home:results', args=(question.id,)))
