# Generated by Django 4.1.6 on 2023-06-05 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0014_questionstatistics_remove_questionstat_question_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionStatistics',
        ),
    ]
