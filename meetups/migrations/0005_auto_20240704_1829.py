# Generated by Django 3.2.25 on 2024-07-04 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20240704_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default=datetime.date(2024, 7, 4)),
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='ysrakeshgupta@gmail.com', max_length=254),
        ),
    ]
