from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    last_Questions = Question.objects.order_by('-pub_date')[:5]
    
    return HttpResponse(', '.join([q.question_text for q in last_Questions]))

def detail(request, question_id):
    return HttpResponse(f'Question {question_id}')

def results(request, question_id):
    return HttpResponse(f'Results {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Vote on Question {question_id}')