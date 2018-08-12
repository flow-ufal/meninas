from django.db import models
from django.utils import timezone
import datetime

""" é a classe das perguntas abertas"""
class OpenQuestion(models.Model):
    name = models.CharField(max_length = 20, help_text="nome da pergunta, para referência")
    questionText = models.CharField(max_length = 500, help_text="O texto da pergunta")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '{0} ({1})'.format(self.name,self.questionText)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Answer(models.Model):
    question = models.ForeignKey("OpenQuestion",
    related_name = "Answer",
    on_delete=models.CASCADE)
    answer = models.CharField("Answer", max_length=500)

    class Meta:
         unique_together = [
            ("question", "answer"),
         ]
