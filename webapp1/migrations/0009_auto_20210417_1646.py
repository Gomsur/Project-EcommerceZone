# Generated by Django 3.1.7 on 2021-04-17 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0008_auto_20210417_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='review_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 17, 16, 46, 8, 6359)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 4, 17, 16, 46, 8, 5360)),
        ),
    ]
