# Generated by Django 3.2.4 on 2021-08-15 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_product_price_range'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_range',
            new_name='prices1',
        ),
    ]