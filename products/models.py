# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'заголовок')
    description = RichTextField(max_length=512, verbose_name=u'описание')
    content = RichTextField(verbose_name=u'полный текст')
    price = models.IntegerField(default=0, verbose_name=u'цена')
    image = models.ImageField(upload_to= 'uploads/bonuses', max_length=256, verbose_name=u'картинка')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Product, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Product.objects.get(slug=page_name)
        except:
            return None
    
    class Meta:
        verbose_name = u'продукт'
        verbose_name_plural = u'продукты'
    
    def __unicode__(self):
        return self.slug