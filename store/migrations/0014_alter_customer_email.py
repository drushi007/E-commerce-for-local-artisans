# Generated by Django 3.2.4 on 2021-06-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_fisrt_name_customer_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]