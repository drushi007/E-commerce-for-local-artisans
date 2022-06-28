from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    password = models.CharField(max_length=200)
    re_enter = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name

    def register(self):
       self.save()

    @staticmethod
    def get_customer_by_email(email1):
        try:

            return Customer.objects.get(email=email1)
        except:
            return False



    def isExists(self):
        if  Customer.objects.filter(email=self.email):
            return True
        return False


