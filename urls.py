from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from form import PostForm
from models import Thread, Post
from views import PostFormView
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(model=Thread), name='forum_home'),
    url(r'^new/$', CreateView.as_view(model=Thread), name='thread_add'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Thread), name='thread_detail'),
    url(r'^(?P<pk>\d+)/new/$', PostFormView.as_view(model=Post, form_class=PostForm), name='post_add'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )