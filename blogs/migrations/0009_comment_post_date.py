# Generated by Django 2.2.4 on 2019-08-25 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]