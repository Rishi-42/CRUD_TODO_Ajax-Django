from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=400)

    def __str__(self):
        return self.firstname