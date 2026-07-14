from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Because every ForeignKey in Django automatically gets two attributes: author      # the related User object
    # author_id   # the integer primary key stored in the database
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title