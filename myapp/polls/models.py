from django.db import models
from django.utils import timezone
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    categories = models.ManyToManyField(Category, related_name='questions', blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    choice_text = models.CharField(max_length=200);
    question = models.ForeignKey(Question, on_delete=models.CASCADE);
    votes = models.IntegerField(default=0);

    def __str__(self):
        return self.choice_text



