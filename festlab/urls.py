# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
    
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^settings/', include('livesettings.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^$', views.home),
    url(r'^call/$', views.call),
    url(r'^request/$', views.request_f),
    url(r'^bonuses/$', views.bonuses),
    url(r'^contacts/$', views.contacts),
    url(r'^about/$', views.about),
    url(r'^products/$', views.products),
    url(r'^products/(?P<page_name>[\w-]+)/$', views.products_in),
    url(r'^services/$', views.services),
    url(r'^(?P<page_name>[\w-]+)/$' , views.page),
    
)
