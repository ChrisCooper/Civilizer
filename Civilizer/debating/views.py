from debating.models import *
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse

def main_page(request):
    return render_to_response('debating/index.html', {})

def main_page_correct(request):
    return render_to_response('debating/index_correct.html', {})

def subject_index(request):
    #order is negative, so it's oldest to newest
    latest_subject_list = Subject.objects.all().order_by('-creation_date')[:5]
    return render_to_response('debating/subject_index.html', {'latest_subject_list': latest_subject_list})

def subject_detail(request, subject_id):
    try:
        s = Subject.objects.get(pk=subject_id)
    except Subject.DoesNotExist:
        raise Http404
    
    points = points_by_subject(subject_id)
    
    return render_to_response('debating/subject_detail.html', {'subject': s,
                                                               'points': points})


#AJAX
def xml_http_request(request):
    if request.is_ajax():
        message = "Hello AJAX"
    else:
        message = "Hello non-AJAX?"
    return HttpResponse(message)