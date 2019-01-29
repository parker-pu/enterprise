from django.db import models


# Create your models here.

class ScrapydHostModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="机器名称")
    describe = models.TextField(verbose_name="描述")
    host = models.CharField(max_length=255, verbose_name="机器地址")
    port = models.IntegerField(verbose_name="机器端口")
    status = models.BooleanField(default=True, verbose_name="机器状态")
    insert_time = models.DateTimeField(auto_now=True, verbose_name="插入时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
