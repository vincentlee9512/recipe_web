# Generated by Django 2.2.4 on 2019-08-21 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('description', models.TextField(blank=True)),
                ('category_1', models.CharField(max_length=100)),
                ('category_2', models.CharField(blank=True, max_length=100)),
                ('category_3', models.CharField(blank=True, max_length=100)),
                ('ingredient', models.TextField()),
                ('step_1', models.TextField()),
                ('step_1_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_2', models.TextField()),
                ('step_2_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_3', models.TextField()),
                ('step_3_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_4', models.TextField()),
                ('step_4_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_5', models.TextField()),
                ('step_5_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_6', models.TextField()),
                ('step_6_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_7', models.TextField()),
                ('step_7_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_8', models.TextField()),
                ('step_8_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_9', models.TextField()),
                ('step_9_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('step_10', models.TextField()),
                ('step_10_photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=False)),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
