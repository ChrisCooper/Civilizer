from debating.models import *
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.core import serializers

from datetime import datetime

def main_page(request):
    return render_to_response('debating/index.html', {})

def subject_index(request):
    #order is negative 'creation_date', so it's oldest to newest
    latest_subject_list = Subject.objects.all().order_by('-creation_date')[:5]
    return render_to_response('debating/subject_index.html', {'latest_subject_list': latest_subject_list})

def subject_detail(request, subject_id):
    try:
        s = Subject.objects.get(pk=subject_id)
    except Subject.DoesNotExist:
        raise Http404
    
    points = points_by_subject(subject_id)
     
    return  render_to_response('debating/subject_detail.html', {'subject': s,
                                                                'points': points})

#AJAX
def post_point(request):
    if request.is_ajax() and request.method == 'POST':
        
        contents = request.POST["point_text"]
      
        print contents
      
        #point = Point()
        #user = User.object.all()[0]
        #subject = Subject.object.all()[0]
        #point.reset(user,subject)
        
        point_representation = "<div>%s</div>" % (contents)
        
        #point_representation = 
        
    
        
        
        #template = loader.get_template('debating/point_inline.html')
        #context = Context({'point': point,\
#                            'user': user})
        #point_representation = template.render(context)
        
        
        data = '{"result": { \
                    "status":"success", \
                    "point_html": "%s" \
                    } \
                }' % (point_representation)
    
    
        print "DATA:::"
        print data

    
        return HttpResponse(data, 'application/javascript')
        #return HttpResponse('{"point": { "user": "Filler User",  "votes": "2",  "upvotes": "3",  "downvotes": "1",  "contents": "This is not live content."}}')
    # If you want to prevent non XHR calls
    else:
        return HttpResponse(status=400)