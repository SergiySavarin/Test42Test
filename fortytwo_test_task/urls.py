from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

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
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'contact'},
        name='auth_logout'),
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='contact')),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='contact'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),
)
urlpatterns += staticfiles_urlpatterns()
