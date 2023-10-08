from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question} 
    
    return render(request, "polls/detail.html", context)





def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
  
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["Choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResonseRedirect(reverse("polls:results", args=(question.id)))











    return HttpResponse("You just voted on question %s." % question_id)

#Testing