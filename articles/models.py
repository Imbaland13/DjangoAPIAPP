from django.db import models
# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length = 100)
    text = models.TextField()
    author = models.CharField(max_length = 30)

class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length = 30)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)