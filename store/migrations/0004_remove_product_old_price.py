# Generated by Django 4.0 on 2021-12-20 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_old_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='old_price',
        ),
    ]