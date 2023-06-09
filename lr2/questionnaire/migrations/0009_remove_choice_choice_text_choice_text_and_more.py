# Generated by Django 4.1.6 on 2023-06-03 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_alter_question_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.question'),
        ),
    ]
