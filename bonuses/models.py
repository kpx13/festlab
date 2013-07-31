# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name=u'заголовок')
    date = models.DateField(verbose_name=u'дата')
    description = models.CharField(max_length=512, verbose_name=u'описание')
    content = RichTextField(verbose_name=u'полный текст')
    image = models.ImageField(upload_to= 'uploads/bonuses', max_length=256, verbose_name=u'картинка')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Article.objects.get(slug=page_name)
        except:
            return None
    
    class Meta:
        verbose_name = u'страница акции'
        verbose_name_plural = u'страница акций'
        ordering = ['-date']
    
    def __unicode__(self):
        return self.slug