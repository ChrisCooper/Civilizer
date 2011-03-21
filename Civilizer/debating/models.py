from django.db import models

class Point(models.Model):
    contents = models.TextField(max_length=1000)
    subject = models.ForeignKey('Subject')
    user = models.ForeignKey('User')
    post_date = models.DateTimeField('date posted')
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    votes = models.IntegerField()
    
    def upvote(self, times=1):
        self.upvotes += times
        self.votes += times
        self.user.upvote(times=times)
        self.user.save()
        self.save()

        
    def downvote(self, times=1):
        self.downvotes += times
        self.votes -= times
        self.user.downvote(times=times)
        self.user.save()
        self.save()
    
    def __unicode__(self):
        str = u"Point on \"" + self.subject.__unicode__() + u"\" by " + self.user.__unicode__()
        str +=  u" (+" + unicode(self.upvotes) + u"/-" + unicode(self.downvotes) + u")"
        return str

class User(models.Model):
    username = models.CharField(max_length=35, unique=True)
    join_date = models.DateTimeField('date joined')
    upvotes = models.IntegerField()
    downvotes = models.IntegerField()
    votes = models.IntegerField()
    
    
    def upvote(self, times=1):
        self.upvotes += times
        self.votes += times
        self.save()
        
    def downvote(self, times=1):
        self.downvotes += times
        self.votes -= times
        self.save()
    
    def get_points(self):
        return Point.objects.filter(user=self.id)
        
    def __unicode__(self):
        return self.username
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    creation_date = models.DateTimeField('date created')
    
    def get_points(self):
        return Point.objects.filter(subject=self.id)
    
    def __unicode__(self):
        return self.name

def points_by_subject(subject):
    return Point.objects.filter(subject=subject)

def points_by_user(user):
    return Point.objects.filter(user=user)