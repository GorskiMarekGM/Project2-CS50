# Generated by Django 3.1.2 on 2020-10-19 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_auto_20201019_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='winner',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]