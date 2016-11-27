from django.conf.urls import include, url

from .views import buildWebsite

urlpatterns = [
    url(r'^go$', buildWebsite),
]