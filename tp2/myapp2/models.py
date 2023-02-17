from django.db import models

# Create your models here.
class Todo(models.Model):
    titre = models.CharField(max_length=30)
    description = models.TextField()
    done = models.BooleanField(default=False)