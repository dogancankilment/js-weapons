from django.conf.urls import patterns, url
# from django.conf import settings

urlpatterns = patterns('',
                       url(r'^d3',
                           'visualization.views.d3',
                           name='d3'),
                       )