from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from .models import *


def index(request):
    questionare_list = Questionario.objects.all()
    context = {'questionare_list': questionare_list}
    return render(request, 'quiz/index.html', context)

def perguntas_dentro_do_questionario(request, questionario_id):
#<QueryDict: {'csrfmiddlewaretoken': ['Ko6cK2zkrCYLyODwOVIZfO8EoZyJJpcizGDpBrjr6Qz6s60WHSVBCN9bHkOzE3e2'],
#'mp_1': [''], 'mp_2': [''], 'op_1': ['blá']}>
    try:
        if request.POST:
            for key in request.POST:
                if "aberta" in key:
                    start = key.find('id') + 2
                    id_ = key[start:]
                    questao = OpenQuestion.objects.get(pk=id_)
                    resposta = Answer(question=questao, answer=request.POST[key])
                    resposta.save()
                elif "fechada" in key:
                    escolha = Choice.objects.get(pk=request.POST[key])
                    escolha.votes += 1
                    escolha.save()
            return HttpResponse('Respostas cadastradas com SUCESSO!')
        else:
            raise ValueError
    except:
        multipleoptionquestion_list = MultipleOptionQuestion.objects.filter(delphis = questionario_id)
        openquestion_list = OpenQuestion.objects.filter(di = questionario_id)
        multipleoptionquestion_dict = {}
        for multipleoptionquestion in multipleoptionquestion_list:
            multipleoptionquestion_dict[multipleoptionquestion] = list(Choice.objects.filter(question = multipleoptionquestion.id))
        context = {"multipleoptionquestion_dict" : multipleoptionquestion_dict,
                   "openquestion_list" : openquestion_list}

        return render(request,'quiz/depois_do_link.html', context)
