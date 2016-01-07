from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.contact.views.contact', name='contact'),
    url(r'^requests/$', 'apps.contact.views.requests', name='requests'),
    url(r'^edit_contact/$', 'apps.contact.views.edit_contact',
        name='edit_contact'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
urlpatterns += staticfiles_urlpatterns()
