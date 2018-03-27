from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^archives/', 'blog.views.archives', name='archives'),

    url(r'^hikkiAdmin/', include(admin.site.urls)),
    url(r'^search/$','blog.views.search',name='search'),
    url(r'^blog/',include('blog.urls')),
    (r'^tinymce/', include('tinymce.urls')),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT
    )
