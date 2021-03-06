# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.simplejson import dumps
from django.views.decorators.cache import cache_page

from call_order.forms import RequestForm
from request.forms import RegisterForm
from bonuses.models import Article
from products.models import Product
from pages.models import Page
from slideshow.models import Slider
from livesettings import config_value
import config


CACHE_TIME=60*60

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['settings'] = { 'email': config_value('MyApp', 'EMAIL'), }
    c.update(csrf(request))
    c['call_form'] = RequestForm()

    return c

"""
def page(request):
    c = get_common_context(request)
    if request.POST and request.POST['action'] == 'call':
        call_form = RequestForm(request.POST)
        if call_form.is_valid():
            call_form.save()
            call_form = RequestForm()
            messages.success(request, u'Спасибо! В ближайшее время мы Вам перезвоним.')
            return HttpResponseRedirect('/')
    else:
        call_form = RequestForm()

    if request.POST and request.POST['action'] == 'request':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            reg_form = RegisterForm()
            messages.success(request, u'Спасибо! Ваша заявка отправлена.')
            return HttpResponseRedirect('/')
    else:
        reg_form = RegisterForm()

    if request.POST and request.POST['action'] == 'review':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            review_form = ReviewForm()
            messages.success(request, u'Спасибо! Ваш отзыв отправлен.')
            return HttpResponseRedirect('/')
    else:
        review_form = ReviewForm()

    c['call_form'] = call_form
    c['reg_form'] = reg_form
    c['review_form'] = review_form
    c['photos'] = Photo.objects.all()
    c['reviews'] = Review.objects.all()
    return render_to_response('base.html', c, context_instance=RequestContext(request))
"""
@cache_page(CACHE_TIME)
def page(request, page_name):
    c = get_common_context(request)

    try:
        c.update(Page.get_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()

"""

    url(r'^about/$', views.about),
    url(r'^products/$', views.products),
    url(r'^products/(?P<page_name>[\w-]+)/$', views.products_in),
    url(r'^services/$', views.services),
"""

@cache_page(CACHE_TIME)
def home(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('home'))
    c['slideshow'] = Slider.objects.all()
    return render_to_response('home.html', c, context_instance=RequestContext(request))


def ajax_call(request):
    if request.is_ajax():
        json_data = {'result': True}
        call_form = RequestForm(request.POST)
        if call_form.is_valid():
            call_form.save()
        else:
            json_data['result'] = False
            json_data['errors'] = call_form.errors
        return HttpResponse(dumps(json_data), mimetype='application/json')


def call(request):
    c = get_common_context(request)
    if request.POST and request.POST['action'] == 'call':
        call_form = RequestForm(request.POST)
        if call_form.is_valid():
            call_form.save()
            call_form = RequestForm()
            #messages.success(request, u'Спасибо! В ближайшее время мы Вам перезвоним.')
            return HttpResponseRedirect(request.POST['next'])
    raise Http404()


def ajax_request(request):
    if request.is_ajax():
        json_data = {'result': True}
        call_form = RegisterForm(request.POST)
        if call_form.is_valid():
            call_form.save()
        else:
            json_data['result'] = False
            json_data['errors'] = call_form.errors
        return HttpResponse(dumps(json_data), mimetype='application/json')


def request_f(request):
    c = get_common_context(request)
    if request.POST and request.POST['action'] == 'request':
        call_form = RegisterForm(request.POST)
        if call_form.is_valid():
            call_form.save()
            call_form = RegisterForm()
            #messages.success(request, u'Спасибо! В ближайшее время мы Вам перезвоним.')
            return HttpResponseRedirect(request.POST['next'])
    raise Http404()


@cache_page(CACHE_TIME)
def bonuses(request):
    c = get_common_context(request)
    c['bonuses'] = Article.objects.all()
    return render_to_response('bonuses.html', c, context_instance=RequestContext(request))


@cache_page(CACHE_TIME)
def bonuses_in(request, page_name):
    c = get_common_context(request)
    c['bonus'] = Article.get_by_slug(page_name)
    return render_to_response('bonuses_in.html', c, context_instance=RequestContext(request))


@cache_page(CACHE_TIME)
def contacts(request):
    c = get_common_context(request)
    return render_to_response('contacts.html', c, context_instance=RequestContext(request))


@cache_page(CACHE_TIME)
def about(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('about'))
    return render_to_response('about.html', c, context_instance=RequestContext(request))


@cache_page(CACHE_TIME)
def products(request):
    c = get_common_context(request)
    c['products'] = Product.objects.all()
    return render_to_response('products.html', c, context_instance=RequestContext(request))


@cache_page(CACHE_TIME)
def products_in(request, page_name):
    c = get_common_context(request)
    c['product'] = Product.get_by_slug(page_name)
    return render_to_response('products_in.html', c, context_instance=RequestContext(request))


@cache_page(CACHE_TIME)
def services(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('services'))
    return render_to_response('services.html', c, context_instance=RequestContext(request))
