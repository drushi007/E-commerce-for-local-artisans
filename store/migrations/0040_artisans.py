# Generated by Django 3.2.4 on 2022-06-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_institute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artisans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=254)),
                ('password', models.CharField(default='', max_length=200)),
                ('re_enter', models.CharField(default='', max_length=200)),
                ('contact', models.CharField(default='', max_length=200)),
                ('shop_location', models.CharField(default='', max_length=200)),
                ('state', models.CharField(default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=100)),
                ('pincode', models.CharField(default='', max_length=10)),
                ('product_name', models.TextField(default='', max_length=100)),
                ('product_info', models.TextField(default='', max_length=100)),
                ('product_image', models.ImageField(default='', upload_to='uploads/artisans_product')),
                ('identity_proof', models.ImageField(default='', upload_to='uploads/artisans_id_proof')),
                ('age', models.TextField(default='', max_length=100)),
            ],
        ),
    ]
