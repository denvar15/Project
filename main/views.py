from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from main.models import Question, Choice

def results(request, question_id):
    field=request.GET.get('field', '')
    xxx = request.GET.get('xxx', '')
    responce="You're looking at the results of questions %s. %s-%s"
    return HttpResponse(responce % (question_id, field, xxx))

def details(request):
    try:
        selected_choice = request.POST['choice']
        pub_date_selected = request.POST['pub_date']
        author_selected = request.POST['author']
    except (KeyError, Choice.DoesNotExist):
        selected_choice = ''
        pub_date_selected = '2018-08-08'
        author_selected = ''
    q = Question()
    q.question_text = selected_choice
    q.pub_date = pub_date_selected
    q.author = author_selected
    q.save()
    return render(request, 'main/details.html', {'selected_choice': selected_choice})

def date(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'main/question.html', {'q': q})

def author(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    x = q.author
    lister = []
    this_author_question_list = Question.objects.order_by('-pub_date')
    context = {'this_author_question_list': this_author_question_list}
    for i in range(len(context['this_author_question_list'])):
        if context['this_author_question_list'][i].author == x:
            lister.append(context['this_author_question_list'][i])
    context2 = {'lister': lister}
    return render(request, 'main/author.html', context2)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'main/index.html', context)


# Create your views here.
