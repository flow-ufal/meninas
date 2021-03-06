# Generated by Django 2.0.6 on 2018-11-26 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=500, verbose_name='Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50, verbose_name='Choice')),
                ('votes', models.IntegerField(default=0)),
                ('position', models.IntegerField(verbose_name='position')),
            ],
        ),
        migrations.CreateModel(
            name='MultipleOptionQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='nome da pergunta, para referência', max_length=15)),
                ('questionText', models.CharField(help_text='O texto da pergunta', max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='A data de publicação')),
            ],
        ),
        migrations.CreateModel(
            name='OpenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='nome da pergunta, para referência', max_length=20)),
                ('questionText', models.CharField(help_text='O texto da pergunta', max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='A data de publicação', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome do Questionario', max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='A data de publicação', null=True)),
                ('questionText', models.CharField(blank=True, help_text='O texto da Questionário', max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='openquestion',
            name='di',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.Questionario'),
        ),
        migrations.AddField(
            model_name='multipleoptionquestion',
            name='delphis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Questionario'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quiz.MultipleOptionQuestion'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Answer', to='quiz.OpenQuestion'),
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('question', 'choice'), ('question', 'position')},
        ),
    ]
