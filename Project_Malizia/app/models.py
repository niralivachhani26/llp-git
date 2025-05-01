from django.db import models

# Create your models here.
class Features(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def get_descriptions(self):
        return self.description.split("\n\n")

