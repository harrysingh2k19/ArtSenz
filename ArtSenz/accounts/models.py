from django.contrib.auth.models import User
from django.db import models

class model_user_article(models.Model):
    """docstring formodel_user_article."""
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    header = models.CharField(max_length=200) #change
    content = models.TextField()
    date =  models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

class model_like_article(models.Model):
    """docstring formodel_user_article."""
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    article = models.ForeignKey(model_user_article, on_delete= models.CASCADE)
    is_like = models.BooleanField(default=False)
    date =  models.DateTimeField(auto_now=True)
