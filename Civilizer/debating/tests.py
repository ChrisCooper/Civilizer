"""
Run "manage.py test".
"""

from django.test import TestCase

from debating.models import *
from datetime import datetime

class SimpleTest(TestCase):
    
    def setUp(self):
        #Subjects
        self.subject = Subject.objects.create(name="Test Subject",\
                                              description="This is a test subject.",\
                                              creation_date=datetime.now())
        
        self.otherSubject = Subject.objects.create(name="Other Subject",\
                                              description="This is another subject.",\
                                              creation_date=datetime.now())
        
        #Users
        self.user = User.objects.create(username="TestUser",\
                                        join_date=datetime.now(),\
                                        upvotes=0,\
                                        downvotes=0,\
                                        votes=0)
        
        self.otherUser = User.objects.create(username="OtherUser",\
                                        join_date=datetime.now(),\
                                        upvotes=0,\
                                        downvotes=0,\
                                        votes=0)
        
        #Points
        self.point = Point.objects.create(contents="This is a test comment",\
                                          subject=self.subject,\
                                          user=self.user,\
                                          post_date=datetime.now(),\
                                          upvotes=0,\
                                          downvotes=0)
        
        self.anotherPoint = Point.objects.create(contents="This is another test comment",\
                                          subject=self.otherSubject,\
                                          user=self.user,\
                                          post_date=datetime.now(),\
                                          upvotes=0,\
                                          downvotes=0)
        
        self.otherPoint = Point.objects.create(contents="This is a different comment",\
                                          subject=self.otherSubject,\
                                          user=self.otherUser,\
                                          post_date=datetime.now(),\
                                          upvotes=0,\
                                          downvotes=0)
        
    def tearDown(self):
        #Subjects
        self.subject.delete()
        self.otherSubject.delete()
        
        #Users
        self.user.delete()
        self.otherUser.delete()
        
        #Points
        self.point.delete
        self.anotherPoint.delete()
        self.otherPoint.delete()
        
class test_vote_counts(SimpleTest):
    def runTest(self):
        """
        Tests whether the vote counts for a user are calculated correctly
        """
        
        self.point.upvote(times=1337)
        self.point.downvote(times=42)
        self.anotherPoint.upvote(times=123)
        self.anotherPoint.downvote(times=456)
        
        self.user = self.point.user
        
        upTotal = self.point.upvotes + self.anotherPoint.upvotes
        downTotal = self.point.downvotes + self.anotherPoint.downvotes
        total = upTotal - downTotal
        
        self.failUnlessEqual(self.user.upvotes, upTotal, "Upvotes wrong")
        self.failUnlessEqual(self.user.downvotes, downTotal, "Downvotes wrong")
        
        self.failUnlessEqual(self.user.votes, total, "Total votes wrong")


class test_user_points(SimpleTest):
    def runTest(self):
        """
        Tests whether the users get points method returns the correct number of points
        """
        points = self.user.get_points()
        self.failUnlessEqual(len(points), 2, "user's get_points failed")

class test_subject_points(SimpleTest):
    def runTest(self):
        """
        Tests whether the subject get points method returns the correct number of points
        """
        points = self.subject.get_points()
        self.failUnlessEqual(len(points), 1, "subjects's get_points failed")

