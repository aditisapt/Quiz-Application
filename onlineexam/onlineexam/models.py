from django.db import models

class Exam(models.Model):
    Questions=models.CharField(max_length=50)
    option1=models.CharField(max_length=50)
    option2=models.CharField(max_length=50)
    option3=models.CharField(max_length=50)
    option4=models.CharField(max_length=50)
    correct=models.CharField(max_length=50)

    class Meta:
        db_table="onlineexam"
        