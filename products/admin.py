# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    search_fields = ('title', 'content')

admin.site.register(models.Product, ProductAdmin)