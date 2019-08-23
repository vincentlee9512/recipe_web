from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    category_1 = models.CharField(max_length=100)
    category_2 = models.CharField(max_length=100, blank=True)
    category_3 = models.CharField(max_length=100, blank=True)
    ingredient = models.TextField()
    step_1 = models.TextField()
    step_1_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_2 = models.TextField(blank=True)
    step_2_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_3 = models.TextField(blank=True)
    step_3_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_4 = models.TextField(blank=True)
    step_4_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_5 = models.TextField(blank=True)
    step_5_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_6 = models.TextField(blank=True)
    step_6_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_7 = models.TextField(blank=True)
    step_7_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_8 = models.TextField(blank=True)
    step_8_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_9 = models.TextField(blank=True)
    step_9_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    step_10 = models.TextField(blank=True)
    step_10_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)


