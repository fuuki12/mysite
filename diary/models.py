from django.db import models
# pythonではdatetime.now だが Djangoではtimezone.nowを使う
from django.utils import timezone


class Day(models.Model):
    # id = models.AutoField(primary_key=True) 内部的に持ってる
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.title