from piston.handler import BaseHandler
from debating.models import Point

class PointHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Point   
    
    def read(self, request, point_id):
        p = Point.objects
        
        point = p.get(id=point_id)
         
        print "point handler read"
        
        return point
    