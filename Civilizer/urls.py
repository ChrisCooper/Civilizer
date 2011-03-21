from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^subjects/$', 'debating.views.subject_index'),
    (r'^subjects/(?P<subject_id>\d+)/$', 'debating.views.subject_detail'),
    (r'^$', 'debating.views.main_page'),
    
    
    #AJAX
    (r'^xml_http_request_test', 'debating.views.xml_http_request'),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    
    #This adds support for static files
    #DO NOT USE IN PRODUCTION
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/Users/chriscooper/Programming/Websites/Civilizer/static'}),
)