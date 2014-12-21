from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^$',
                           'visualization.views.index',
                           name='index'),
                       url(r'^sunburst$',
                           'visualization.views.sunburst',
                           name='sunburst'),
                      )
