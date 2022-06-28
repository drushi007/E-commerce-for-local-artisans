from django.db import models


class Signup(models.Model):
    image = models.ImageField(upload_to='uploads/products')



    @staticmethod
    def get_all_images():
        return Signup.objects.all()

