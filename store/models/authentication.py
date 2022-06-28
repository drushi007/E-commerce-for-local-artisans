from django.db import models
class Auth(models.Model):
    name=models.CharField(max_length=500,default='')
    info=models.TextField(max_length=100000)
    image=models.ImageField(upload_to='store/info', default='')

    def __str__(self):
        return self.name
    @staticmethod
    def auth_get_all():
        return Auth.objects.all()