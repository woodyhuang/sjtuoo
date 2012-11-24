#coding: utf-8

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(u'名称', max_length=64)
    
    class Meta:
        db_table = 'product_category'
        verbose_name = u'产品类别'
        verbose_name_plural = u'产品类别'
