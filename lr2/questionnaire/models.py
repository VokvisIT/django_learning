from django.db import models

class DataSet(models.Model):
    TYPE_SELECT = (
        ('0', 'Female'),
        ('1', 'Male'),
    )
    gender = models.CharField(max_length=11,choices=TYPE_SELECT, default=0)
    open_question = models.TextField(null=False, blank=True)

