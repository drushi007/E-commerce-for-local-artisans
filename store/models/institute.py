from django.db import models


class Institute(models.Model):
    name = models.CharField(max_length=200,default='',blank=False)
    state=models.CharField(max_length=200,default='',blank=False)
    city=models.CharField(max_length=200,default='',blank=False)
    address=models.CharField(max_length=10000,default='')
    aicte_rank=models.CharField(max_length=10,default='')
    department_no=models.CharField(max_length=10,default='')
    courses_offered=models.CharField(max_length=200,default='')
    students_capacity=models.CharField(max_length=20,default='')


    def register(self):
       self.save()







