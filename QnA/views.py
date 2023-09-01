from django.shortcuts import render
from .models import Question
from .forms import QuestionForm
# Create your views here.

def index(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'index.html', context)

def question(request, q_id):
    question = Question.objects.get(id=q_id)
    # if request.method == 'POST':
    #     pass
    # else:
        
    context = {
        'question': question,
    }

    return render(request, 'question.html', context)