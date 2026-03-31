from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Analyze(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    tool_type = models.CharField(max_length=50)
    analyze_text = models.TextField()
    word_count = models.IntegerField(default=0)
    sentiment_score = models.FloatField(default=0.0)
    sentiment_label = models.CharField(max_length=20, default="Neutral")
    pos_score = models.FloatField(default=0)
    neg_score = models.FloatField(default=0)
    neu_score = models.FloatField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True)
    summary_text = models.TextField(null=True, blank=True)
    keyword_text = models.TextField(null=True, blank=True)