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
