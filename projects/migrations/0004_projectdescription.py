# Generated by Django 2.2.4 on 2019-10-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190930_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
