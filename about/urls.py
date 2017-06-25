# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^add/', views.add, name='add'),
    url('^new_add/(\d+)/(\d+)/$', views.new_add, name='calc_add'),
    url('^index(?:.html)?$', views.about_index, name='about'),
    url('^todo$', views.about_todo),
    url('^todo/(?P<n>\w{0,50})/$', views.about_detail),
]
