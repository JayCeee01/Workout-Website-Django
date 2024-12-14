from django.db import models

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='workouts/')
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

