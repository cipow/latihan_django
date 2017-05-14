from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', publish, name='publish'),
    url(r'^page/(?P<page>[0-9]+)/$', publish_page, name='page'),
]
