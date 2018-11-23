from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /quiz/5/
    path('<int:questionario_id>/', views.perguntas_dentro_do_questionario, name='depois_questionario'),
    # ex: /quiz/5/results/
]
