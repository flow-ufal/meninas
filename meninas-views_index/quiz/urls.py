from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:multipleoptionquestion_id>/',views.perguntas_dentro_do_questionario, name = 'depois_do_link'),
    path('<int:multipleoptionquestion_id>/', views.detail, name='detail'),
    # ex: /quiz/5/results/

]
