from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    rating = models.CharField(max_length=5, default='')
    experience = models.TextField(max_length=500)
    improve = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def register_feedback(self):
        self.save()
