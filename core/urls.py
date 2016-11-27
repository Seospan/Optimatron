from django.conf.urls import include, url

from .views import TestView, SnippetListView, SnippetDetailView
from .views import index, testid

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^test/', TestView.as_view()),
    #url(r'^test/$', test),
    url(r'^test/(?P<id>[0-9]*)$', testid),
    url(r'^snippets/$', SnippetListView.as_view()),
    url(r'^snippets/(?P<pk>[0-9]*)$', SnippetDetailView.as_view(), name="snippet-detail"),
    #url(r'^build/', buildWebsite),
    url(r'^build/', include('builder.urls')),
]