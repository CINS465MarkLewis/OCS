from django.db import models
from django.contrib.auth.models import User

class University(models.Model):
    uniName = models.CharField(max_length=50) #uniName
    uniLoca = models.CharField(max_length=50) #uniLocation
    uniLogo = models.CharField(max_length=1000) #uniLogo

class Org(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    #University may need to be removed

    orgName = models.CharField(max_length=50) #orgName
    orgCateg = models.CharField(max_length=50) #orgCategory
    orgUni = models.CharField(max_length=100) #orgUniversity
    orgFoun = models.CharField(max_length=30) #orgFounded
    orgLogo = models.CharField(max_length=1000) #orgLogo

class Chat(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message
