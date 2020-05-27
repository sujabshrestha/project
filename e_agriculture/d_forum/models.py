from django.db import models

# Create your models here.
class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=100)
    question_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=20)

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    aid = models.AutoField(primary_key = True)
    qid = models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.CharField(max_length=20)