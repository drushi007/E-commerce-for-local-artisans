# Generated by Django 3.2.4 on 2022-06-03 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_shipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='artisan_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.artisans'),
        ),
    ]
