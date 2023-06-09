# Generated by Django 4.2.2 on 2023-06-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0022_remove_answer_num_of_comp_poll_count_comp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='count_comp',
            new_name='completed_count',
        ),
        migrations.RemoveField(
            model_name='question',
            name='num_answers',
        ),
        migrations.AddField(
            model_name='choice',
            name='answer_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='poll',
            name='poll_title',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
