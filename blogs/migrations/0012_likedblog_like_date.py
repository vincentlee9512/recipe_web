# Generated by Django 2.2.4 on 2019-08-26 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_remove_likedblog_like_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='likedblog',
            name='like_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
