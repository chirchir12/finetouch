# Generated by Django 2.2.4 on 2019-09-09 14:47

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=pages.models.upload_image_to)),
                ('content', models.TextField()),
            ],
        ),
    ]
