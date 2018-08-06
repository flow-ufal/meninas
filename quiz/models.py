from django.db import models

""" é a classe das perguntas abertas"""
class OpenQuestion(models.Model):
    name = models.CharField(max_length = 20, help_text="nome da pergunta, para referência")
    questionText = models.CharField(max_length = 500, help_text="O texto da pergunta")

    def __str__(self):
        return '{0} ({1})'.format(self.name,self.questionText)

class Answer(models.Model):
    question = models.ForeignKey("OpenQuestion",
    related_name = "Answer",
    on_delete=models.CASCADE)
    answer = models.CharField("Answer", max_length=500)

# Create your models here.
