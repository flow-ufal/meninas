from django.shortcuts import render

from .models import Questionario


def index(request):
    latest_questionare_list = Questionario.objects.order_by('-pub_date')[:5]
    context = {'latest_questionare_list': latest_questionare_list}
    return render(request, 'quiz/index.html', context)

