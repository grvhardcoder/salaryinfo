from django.conf.urls import patterns, include, url
from django.contrib import admin
#from salary import settings 
#from salarylive.views import signup
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'salary.views.home', name='home'),
    #url(r'^salary/', include('salary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'salarylive.views.signup'),
)
