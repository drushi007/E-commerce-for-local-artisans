# Generated by Django 3.2.4 on 2021-08-14 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_order_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]