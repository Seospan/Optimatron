from django.conf.urls import url

from .views import TestView
from .views import index, testid

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^test/', TestView.as_view()),
    #url(r'^test/$', test),
    url(r'^test/(?P<id>[0-9]*)$', testid),
]