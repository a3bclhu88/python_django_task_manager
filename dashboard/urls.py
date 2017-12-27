'''
Created on Dec 18, 2017

@author: Andy
'''

from django.conf.urls import url

from . import views

urlpatterns=[
        url(r'^$',views.index, name='index'),
       
    ];