from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from .models import Questionario, MultipleOptionQuestion, OpenQuestion


def index(request):
    questionare_list = Questionario.objects.all()
    context = {'questionare_list': questionare_list}
    return render(request, 'quiz/index.html', context)

def perguntas_dentro_do_questionario(request, questionario_id):
    multipleopenquestion_list = MultipleOptionQuestion.objects.filter(delphis = questionario_id)
    choice_list = MultipleOptionQuestion.objects.filter(choices = questionario_id)
    openquestion_list = OpenQuestion.objects.filter(di = questionario_id)
    context = {"multipleopenquestion_list" : multipleopenquestion_list,
                "openquestion_list" : openquestion_list,
                "choice_list" : choice_list}

    return render(request,'quiz/depois_do_link.html', context)
