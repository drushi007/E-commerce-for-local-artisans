from django.db import models


class Volunteer(models.Model):
    first_name = models.CharField(max_length=200, default='')
    last_name = models.CharField(max_length=200, default='')
    email = models.EmailField(default='')
    password = models.CharField(max_length=200, default='')
    re_enter = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    address_optional = models.CharField(max_length=100, default='')
    pincode = models.CharField(max_length=10, default='')
    motive = models.TextField(max_length=100, default='')

    @staticmethod
    def get_all_images1():
        return Volunteer.objects.all()

    def register1(self):
        self.save()

    @staticmethod
    def get_volunteer_by_email(email1):
        try:

            return Volunteer.objects.get(email=email1)
        except:
            return False



    def isExists1(self):
        if Volunteer.objects.filter(email=self.email):
            return True
        return False
