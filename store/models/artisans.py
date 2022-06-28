from django.db import models


class Artisans(models.Model):
    name = models.CharField(max_length=200, default='')

    email = models.EmailField(default='')
    password = models.CharField(max_length=200, default='')
    re_enter = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=200, default='')
    shop_location = models.CharField(max_length=200, default='')
    state = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
    pincode = models.CharField(max_length=10, default='')
    product_name = models.TextField(max_length=100, default='')
    product_info = models.TextField(max_length=100, default='')
    product_image = models.ImageField(upload_to='uploads/artisans_product',default='')
    price=models.CharField(max_length=100, default='')
    identity_proof = models.ImageField(upload_to='uploads/artisans_id_proof', default='')
    age = models.TextField(max_length=100, default='')
    status=models.BooleanField(default=False)

    def isExists1(self):
        if Artisans.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_artisans_by_email(email1):
        try:

            return Artisans.objects.get(email=email1)
        except:
            return False







    def register1(self):
        self.save()