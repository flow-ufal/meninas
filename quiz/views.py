from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from .models import Questionario, MultipleOptionQuestion, OpenQuestion, Choice


def index(request):
    questionare_list = Questionario.objects.all()
    context = {'questionare_list': questionare_list}
    return render(request, 'quiz/index.html', context)

def perguntas_dentro_do_questionario(request, questionario_id):
    multipleoptionquestion_list = MultipleOptionQuestion.objects.filter(delphis = questionario_id)
    openquestion_list = OpenQuestion.objects.filter(di = questionario_id)
    multipleoptionquestion_dict = {}
    for multipleoptionquestion in multipleoptionquestion_list:
        multipleoptionquestion_dict[multipleoptionquestion] = list(Choice.objects.filter(question = multipleoptionquestion.id))
    context = {"multipleoptionquestion_dict" : multipleoptionquestion_dict,
               "openquestion_list" : openquestion_list}

    return render(request,'quiz/depois_do_link.html', context)

