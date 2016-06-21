from django.db import models
from django.contrib.auth.models import User, UserManager
import datetime
# Create your models here.



class QuestionManager(models.Manager):
	def newest(self):
		return self.order_by('-id')
	def hot(self):
		return self.order_by('-rating')

class CustomUser(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to = '/uploads/')
	rating = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __unicode__(self):
		return self.name



class Question(models.Model):
	user = models.ForeignKey(CustomUser)
	title = models.CharField(max_length = 255)
	tags = models.ManyToManyField(Tag)
	text = models.TextField()
	rating = models.IntegerField(default=0,db_index = True)
	created = models.DateTimeField(default=datetime.datetime.now)
	objects = QuestionManager()
	def __unicode__(self):
		return self.title


class Answer(models.Model):
	user = models.ForeignKey(CustomUser)
	question = models.ForeignKey(Question)
	text = models.TextField()
	created = models.DateTimeField(default=datetime.datetime.now)
	rating = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.text		

class QuestionLike(models.Model):
    user_ptr = models.ForeignKey(CustomUser)
    likeType = models.IntegerField(default=0) #can be -1, 0, 1
    question = models.ForeignKey(Question)
    class Meta:
        unique_together = ('user_ptr', 'question',)


class AnswerLike(models.Model):
    user_ptr = models.ForeignKey(CustomUser)
    likeType = models.IntegerField(default=0)
    answer = models.ForeignKey(Answer)
    class Meta:
        unique_together = ('user_ptr', 'answer',)
