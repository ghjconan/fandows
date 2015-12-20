"""
Definition of urls for fdproxy.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from httpproxy.views import HttpProxy


urlpatterns = patterns('',
    (r'^proxy/(?P<url>.*)$', HttpProxy.as_view(base_url='http://www.google.com/')),
)
