from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
# Create your views here.

def index(request):
    questions = Question.objects.all()
    first_question = Question.objects.get(id=1)

    context = {
        'questions': questions,
        'q_id': first_question.id,
    }

    return render(request, 'index.html', context)



def question(request, q_id):
    question = Question.objects.get(id=q_id)
    
    context = {
        'question': question,
        'q_id' : question.id,
        
    }

    return render(request, 'question.html', context)




def next_question(request, q_id):
    next_question = Question.objects.get(id=2)



    return redirect(f'/QnA/{next_question.id}/')