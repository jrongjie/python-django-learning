from django.db import models

# Create your models here.
class todoList(models.Model):
    text = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text