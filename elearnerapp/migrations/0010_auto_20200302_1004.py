# Generated by Django 2.1.2 on 2020-03-02 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearnerapp', '0009_auto_20200302_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionnaire',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='ques',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Questionnaire',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
