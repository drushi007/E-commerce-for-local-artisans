# Generated by Django 3.2.4 on 2021-06-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='re_enter',
            field=models.CharField(default='', max_length=200),
        ),
    ]
