from django.db import models


class About(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    image=models.ImageField(upload_to='uploads/users',default='')
    def __str__(self):
        return self.name

    @staticmethod
    def about_all_users():
        return About.objects.all()
