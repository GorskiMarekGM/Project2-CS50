# Generated by Django 3.1.2 on 2020-10-08 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_remove_photo_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction',
            old_name='photo',
            new_name='photos',
        ),
    ]