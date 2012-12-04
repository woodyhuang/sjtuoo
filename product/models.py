#coding: utf-8

from django.db import models


class Product(models.Model):
    name = models.CharField(u'名称', max_length=64)
    price = models.CharField(u'价格',max_length=64)
    imgurl = models.CharField(u'图片Url',max_length=128)
    
    class Meta:
        db_table = 'product'
        verbose_name = u'产品'
        verbose_name_plural = u'产品'
