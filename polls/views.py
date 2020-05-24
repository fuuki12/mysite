from django.shortcuts import get_object_or_404, render

from .models import Question
from django.http import Http404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})
    
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return render(response % question_id)

def vote(request, question_id):
    return render("You're voting on question %s." % question_id)