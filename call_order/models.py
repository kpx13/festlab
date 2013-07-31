# -*- coding: utf-8 -*-
from django.db import models
from pytils import dt

class Request(models.Model):
    name  = models.CharField(u'имя', blank=True, max_length=255)
    phone  = models.CharField(u'телефон', blank=True, max_length=255)
    request_date = models.DateTimeField(u'дата заявки', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'заявка на обратный звонок'
        verbose_name_plural = u'заявки на обратный звонок'
        ordering = ['-request_date']

    def __unicode__(self):
        return u'№ %s от %s' % (self.id, dt.ru_strftime(u"%d %B %Y", self.request_date))
