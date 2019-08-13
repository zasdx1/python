from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello, wodddrld")

def detail(request, question_id):
    return HttpResponse("you're looking at question %s." %question_id)

def results(request, question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("your're voting on question %s" % question_id)


