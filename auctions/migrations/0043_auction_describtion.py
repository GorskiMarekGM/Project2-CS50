# Generated by Django 3.1.2 on 2020-12-23 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0042_remove_auction_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='describtion',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
    ]
