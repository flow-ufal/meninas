from django.contrib import admin

from .models import OpenQuestion, Answer, Questionario, MultipleOptionQuestion, Choice

admin.site.register(MultipleOptionQuestion)
admin.site.register(Choice)
admin.site.register(Questionario)
admin.site.register(OpenQuestion)
admin.site.register(Answer)

# Register your models here.
