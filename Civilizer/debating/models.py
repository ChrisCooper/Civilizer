from django.db import models

class Point(models.Model):
    contents = models.TextField(max_length=1000)
    subject = models.ForeignKey(Subject)
#    subject_contribution = models.ForeignKey(SubjectContribution)
    poster = models.ForeignKey(User)
    post_date = models.DateTimeField('date published')
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=35)
    join_date = models.DateTimeField('date joined')
    total_upvotes = models.IntegerField()
    total_downvotes = models.IntegerField()
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    creation_date = models.DateTimeField('date created')
    
#class SubjectContribution(models.Model):
#   user = models.ForeignKey(User)
#    subject = models.ForeignKey(Subject)
#    total_upvotes = models.IntegerField()
#    total_downvotes = models.IntegerField()