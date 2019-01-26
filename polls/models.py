import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __repr__(self):
        return "Question: {0}\nDate: {1}".format(
            self.question_text,
            self.pub_date,
        )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __repr__(self):
        return "Choice: {0} for the question: {1}\nNumber of votes: {2}".format(
            self.choice_text,
            self.question,
            self.votes,
        )