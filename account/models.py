#coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class ContactAddress(models.Model):
    user = models.ForeignKey(User)
    contact_name = models.CharField(u'联系人', max_length=64)
    phone = models.CharField(u'电话', max_length=32)
    post_code = models.CharField(u'邮编', max_length=6)
    address = models.CharField(u'详细地址', max_length=128)
    is_default = models.BooleanField(u'设为默认地址', default=False)
    
    class Meta:
        db_table = 'account_contact'
#        app_label = u'账号额外信息'
        verbose_name = u'送货地址'
        verbose_name_plural = u'送货地址'

    def __unicode__(self):
        return u'%(name)s(%(phone)s)， %(address)s， %(post_code)s' % {
                               'name': self.contact_name,
                               'phone': self.phone,
                               'address': self.address,
                               'post_code': self.post_code,
                               }
        
     ###### extra colume in admin list #####
    def owner_link(self):
        return '<a href="/admin/auth/user/%s/">%s</a>' % (self.user.id, self.user.username)
    owner_link.allow_tags = True
    owner_link.short_description = u'所属账号'
