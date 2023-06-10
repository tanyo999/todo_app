from django.db import models

class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(blank=False)
    Completed = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
# Create your models here.
