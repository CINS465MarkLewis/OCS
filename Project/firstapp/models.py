from django.db import models

# Create your models here.
class suggestion(models.Model):
    suggestion = models.CharField(max_length=30)

    def __str__(self):
        return self.suggestion
