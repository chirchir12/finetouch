# Generated by Django 2.2.4 on 2019-09-09 16:03

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='content', max_length=150),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_to_category),
        ),
    ]
