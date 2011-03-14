from debating.models import *
from django.shortcuts import render_to_response

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
