from django.db import models
import uuid
from users.models import Profile
class project(models.Model):
    owner = models.ForeignKey(Profile, null= True,blank= True, on_delete = models.CASCADE)
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length= 2000, null= True, blank= True)
    featured_image = models.ImageField(null=True,blank=True , default ="default.jpg" )
    Demo_link = models.CharField(max_length= 2000, null= True, blank= True)
    Source_link = models.CharField(max_length= 2000, null= True, blank= True)
    Tags = models.ManyToManyField("tag")
    Vote_total = models.IntegerField(default= 0)
    vote_ratio = models.IntegerField(default= 0)
    Created = models.TimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return self.Title
    class Meta:
        ordering = ['-vote_ratio','-Vote_total','Title']

    @property
    def imageURL(self):
        try :
            url = self.featured_image.url
        except:
            url = ''
        return url
    
    @property
    def reviewers(self):
        queryset = self.reviews_set.all().values_list('owner__id',flat = True)
        return  queryset

    @property
    def getVoteCount(self):
        review = self.reviews_set.all()
        upVotes = review.filter(Value = 'up').count()
        totalVotes = review.count()
        ratio = (upVotes/totalVotes)*100
        self.Vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

class Reviews(models.Model):

    vote = (("up","up vote"),
            ("down","down vote"))

    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    Project = models.ForeignKey(project,on_delete=models.CASCADE)
    Body = models.TextField(max_length= 2000, null= True, blank= True)
    Value = models.CharField(choices= vote,max_length= 50)

    Created = models.TimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    class Meta:
        unique_together = [['owner','Project']]
    def __str__(self):
        return self.Value
    

class tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    def __str__(self):
        return self.name
    

