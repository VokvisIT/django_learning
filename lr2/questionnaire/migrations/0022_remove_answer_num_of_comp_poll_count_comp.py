# Generated by Django 4.1.6 on 2023-06-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0021_answer_num_of_comp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='num_of_comp',
        ),
        migrations.AddField(
            model_name='poll',
            name='count_comp',
            field=models.IntegerField(default=0),
        ),
    ]
