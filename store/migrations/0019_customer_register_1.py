# Generated by Django 3.2.4 on 2021-06-15 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='register_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.register'),
        ),
    ]
