import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    # def __repr__(self):
    #     return "Question: {0}\nDate: {1}".format(
    #         self.question_text,
    #         self.pub_date,
    #     )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    # def __repr__(self):
    #     return "Choice: {0} for the question: {1}\nNumber of votes: {2}".format(
    #         self.choice_text,
    #         self.question,
    #         self.votes,
    #     )
