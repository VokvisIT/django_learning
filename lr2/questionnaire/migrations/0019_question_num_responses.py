# Generated by Django 4.1.6 on 2023-06-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0018_question_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='num_responses',
            field=models.IntegerField(default=0),
        ),
    ]
