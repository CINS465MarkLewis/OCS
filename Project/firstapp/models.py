from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class University(models.Model):
    uniName = models.CharField(max_length=50) #uniName
    uniLoca = models.CharField(max_length=50) #uniLocation
    uniLogo = models.CharField(max_length=1000) #uniLogo

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.uniName + ' in ' + self.uniLoca

class Org(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    #University may need to be removed, key for DB entry tied to Uni
    orgName = models.CharField(max_length=50) #orgName
    orgCateg = models.CharField(max_length=50) #orgCategory
    orgFoun = models.CharField(max_length=30) #orgFounded
    orgLogo = models.CharField(max_length=1000) #orgLogo

    def __str__(self):
        return self.orgName

class Chat(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message

class Question(models.Model):
    question_text = models.CharField(max_length = 100)
    date = models.DateTimeField("published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length = 100)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
