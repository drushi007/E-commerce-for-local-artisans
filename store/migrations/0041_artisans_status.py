# Generated by Django 3.2.4 on 2022-06-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_artisans'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisans',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]