from django.db import models
from django.utils import timezone
import datetime

#from django.forms import ModelChoiceField
#from django.forms import ModelMultipleChoiceField

#class Choice(models.Model):
#    choiceName = models.CharField(max_length = 20, help_text = "O nome da opção, para referência do administrador")
#    choiceText = models.CharField(max_length = 500, help_text = "O texto da opção, que o usuário irá ler")

#class MultipleOptionQuestion(ModelChoiceField): precisa estudar modelforms

#é a classe das perguntas de multipla escolha

class Questionario(models.Model):
    name = models.CharField(max_length = 50, help_text="Nome do Questionario")


class MultipleOptionQuestion(models.Model):
    delphis = models.ForeignKey(
       Questionario,
       on_delete=models.CASCADE,
    )
    name = models.CharField(max_length = 15, help_text="nome da pergunta, para referência")
    questionText = models.CharField(max_length = 500, help_text="O texto da pergunta")
    pub_date = models.DateTimeField(auto_now_add = True, help_text="A data de publicação")

    def __str__(self):
        return '{0} ({1})'.format(self.name,self.questionText)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


#dessa forma, você poderá criar várias respostas que poderão
#ser usadas em váris respostas diferentes, o que é conveniente
#para perguntas de sim ou não, ou perguntas de muito bom, muito ruim, etc
class Choice(models.Model):
     question = models.ForeignKey(
        "MultipleOptionQuestion",
        related_name="choices",
        on_delete=models.CASCADE,
     )
     choice = models.CharField("Choice", max_length=50)
     votes = models.IntegerField(default=0)
     position = models.IntegerField("position")


     class Meta:
         unique_together = [
            ("question", "choice"),
            ("question", "position")
         ]
ordering = ("position",)


""" é a classe das perguntas abertas"""
class OpenQuestion(models.Model):
    di = models.ForeignKey(
       "Questionario",
       related_name="questions",
       on_delete=models.CASCADE,
    )
    name = models.CharField(max_length = 20, help_text="nome da pergunta, para referência")
    questionText = models.CharField(max_length = 500, help_text="O texto da pergunta")
    pub_date = models.DateTimeField(auto_now_add = True, help_text="A data de publicação", null= True, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.name,self.questionText)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
    question = models.ForeignKey("OpenQuestion",
    related_name = "Answer",
    on_delete=models.CASCADE)
    answer = models.CharField("Answer", max_length=500)

# Create your models here.
