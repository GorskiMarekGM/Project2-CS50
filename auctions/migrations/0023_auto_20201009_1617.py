# Generated by Django 3.1.2 on 2020-10-09 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20201009_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='auction',
            field=models.ManyToManyField(related_name='auctions', to='auctions.Auction'),
        ),
    ]