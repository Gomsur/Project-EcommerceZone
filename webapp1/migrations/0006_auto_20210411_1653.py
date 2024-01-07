# Generated by Django 3.1.7 on 2021-04-11 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0005_auto_20210411_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='Your_has_been_packed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='Your_order_is_on_the_way',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 11, 16, 53, 22, 607108)),
        ),
    ]
