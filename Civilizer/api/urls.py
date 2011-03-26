from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import PointHandler


point_handler = Resource(PointHandler)

urlpatterns = patterns('',
    (r'^points/(?P<point_id>\d+)$', point_handler),
)

