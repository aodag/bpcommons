#:coding=utf-8:
from django.conf.urls.defaults import *
from django.conf import settings

from commons.tests.views_tests import TestViews

urlpatterns = patterns('',
    (r'', include(TestViews().urls)),
    (r'json_response', 'commons.tests.http.test_json_response'),
)
