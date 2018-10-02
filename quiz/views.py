from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from .models import Questionario, MultipleOptionQuestion, OpenQuestion


def index(request):
    latest_questionare_list = Questionario.objects.order_by('-pub_date')[:5]
    context = {'latest_questionare_list': latest_questionare_list}
    return render(request, 'quiz/index.html', context)

def perguntas_dentro_do_questionario(request, multipleoptionquestion_id):
    multipleopenquestion_list = MultipleOptionQuestion.objects.filter(delphis = multipleoptionquestion_id)
    context = {"multipleopenquestion_list" : multipleopenquestion_list}

    return render(request,'quiz/depois_do_link.html', context)

def detail(request, multipleoptionquestion_id):
    try:
        list = Questionario.objects.get(multipleoptionquestion=multipleoptionquestion_id)
    except Questionario.DoesNotExist:
        raise Http404("Questionario does not exist")
    return render(request, 'quiz/detail.html', {'list': list})

def results(request, questionario_id):
    response = "You're looking at the results of questionare %s."
    return HttpResponse(response % questionario_id)

def vote(request, questionario_id):
    return HttpResponse("You're voting on question %s." % questionario_id)
