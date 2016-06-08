from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'db_monitor_query.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^login/','querystat.views.login',name='index'),
    url(r'^validate/','querystat.views.validateUser',name='validateUser'),
    url(r'^logout/','querystat.views.logout',name='logout'),
    url(r'^pstat/','querystat.views.getPstat',name='getPstat'),
    url(r'^filterpstat/','querystat.views.filterPstat',name='filterPstat'),
)


from django.conf import settings
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )
