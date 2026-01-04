from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    isPublic = models.BooleanField(default=True)

    def __str__(self):
        return self.title