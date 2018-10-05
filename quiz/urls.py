from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /quiz/5/
    path('<int:questionario_id>/', views.detail, name='detail'),
    # ex: /quiz/5/results/
    path('<int:questionario_id>/results/', views.results, name='results'),
    # ex: /quiz/5/vote/
    path('<int:questionario_id>/vote/', views.vote, name='vote'),
]
#Chatuba
