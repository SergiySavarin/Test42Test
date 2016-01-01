from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.contact.views.contact', name='contact'),
    # url(r'^requests/$', 'apps.contact.views.requests', name='requests'),
    url(r'^admin/', include(admin.site.urls)),
)
