#coding: utf-8

from django.db import models
from django.contrib.auth.models import User

from product.models import Product


ORDER_STATUS = (('1', u'新提交'),
                  ('2', u'商品出库'),
                  ('3', u'等待收货'),
                  ('4', u'完成'),
                  )

class Order(models.Model):
    amount = models.FloatField(u'总价')
    owner = models.ForeignKey(User, verbose_name=u'客户')
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    status = models.CharField(u'状态', max_length=1, choices=ORDER_STATUS, default='1')
    address = models.TextField(u'送货地址')
    description = models.TextField(u'额外说明', blank=True, null=True)
    
    class Meta:
        db_table = 'order'
        verbose_name = u'订单'
        verbose_name_plural = u'订单'
        app_label = u'客户订单'
    
    def __unicode__(self):
        return self.number

    @property
    def number(self):
        return 'OSN-%d' % self.id
    
    @property
    def is_new(self):
        return '1' == self.status


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'订购商品')
    price = models.FloatField(u'单价')
    count = models.PositiveIntegerField(u'数量')
    order = models.ForeignKey(Order, verbose_name=u'订单编号')
    
    class Meta:
        db_table = 'order_item'
        verbose_name = u'所购商品'
        verbose_name_plural = u'所购商品'
    
    def __unicode__(self):
        return self.product.name
    
    @property
    def amount(self):
        return self.count * self.price
    