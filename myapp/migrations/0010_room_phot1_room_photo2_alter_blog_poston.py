# Generated by Django 4.0.1 on 2023-05-19 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_booking_status_booking_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='phot1',
            field=models.ImageField(default='', upload_to='blog/'),
        ),
        migrations.AddField(
            model_name='room',
            name='photo2',
            field=models.ImageField(default='', upload_to='blog/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='poston',
            field=models.DateField(default=datetime.date(2023, 5, 19)),
        ),
    ]
