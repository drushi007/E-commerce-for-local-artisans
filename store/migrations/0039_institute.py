# Generated by Django 3.2.4 on 2022-03-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_order_delivery_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('state', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=10000)),
                ('aicte_rank', models.CharField(default='', max_length=10)),
                ('department_no', models.CharField(default='', max_length=10)),
                ('courses_offered', models.CharField(default='', max_length=200)),
                ('students_capacity', models.CharField(default='', max_length=20)),
            ],
        ),
    ]