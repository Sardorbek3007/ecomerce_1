# Generated by Django 4.0 on 2021-12-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(default=None, null=True, upload_to='photoes/products'),
        ),
    ]
