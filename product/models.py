#coding: utf-8

from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(u'名称', max_length=64)
    
    class Meta:
        db_table = 'product_category'
        verbose_name = u'产品类别'
        verbose_name_plural = u'产品类别'
    
    def __unicode__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(u'名称', max_length=64)
    image = models.FileField(u'示意图', upload_to='photos/product/%Y/%m/%d')
    category = models.ForeignKey(ProductCategory, verbose_name=u'类别')
    price = models.FloatField(u'单价')
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    description = models.TextField(u'描述')
    
    class Meta:
        db_table = 'product'
        verbose_name = u'产品'
        verbose_name_plural = u'产品'
    
    def __unicode__(self):
        return self.name
