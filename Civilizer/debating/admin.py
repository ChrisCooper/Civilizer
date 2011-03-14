from models import *
from django.contrib import admin

class PointAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['subject', 'user', 'contents']}),
        ('Pre-determined information', {'fields': ['post_date', 'upvotes', 'downvotes']}),
    ]
    list_display = ('user', 'subject', 'post_date', 'upvotes', 'downvotes')
    list_filter = ['post_date']
    search_fields = ['contents']
    date_hierarchy = 'post_date'
    
class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'description']}),
        ('Pre-determined information', {'fields': ['creation_date']}),
    ]
    list_display = ('name', 'creation_date')
    list_filter = ['creation_date']
    search_fields = ['name' 'description']
    date_hierarchy = 'creation_date'

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['username']}),
        ('Pre-determined information', {'fields': ['join_date', 'upvotes', 'downvotes', 'votes']}),
    ]
    list_display = ('username', 'join_date', 'votes')
    list_filter = ['join_date']
    search_fields = ['username']
    date_hierarchy = 'join_date'  
    
admin.site.register(Subject, SubjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Point,PointAdmin)