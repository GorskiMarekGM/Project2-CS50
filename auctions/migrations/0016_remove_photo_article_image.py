# Generated by Django 3.1.2 on 2020-10-08 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201008_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='article_image',
        ),
    ]
