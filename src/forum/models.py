from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.db.models import Q

# Create your models here.

User = settings.AUTH_USER_MODEL


class QuestionQuerySet(models.query.QuerySet):
	def search(self, query):
		if query:
			query = query.strip()
			return self.filter(
				Q(title__icontains=query)|
				Q(question__icontains=query)
				).distinct()
		return self


class QuestionManager(models.Manager):

	def get_queryset(self):
		return QuestionQuerySet(self.model, using=self._db)


class Question(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	question = models.TextField(help_text='Separate by a Comma')
	image = models.ImageField(null=True, blank= True, height_field = "height_field", width_field = "width_field" )
	height_field = 	models.IntegerField(default= 0)
	width_field = models.IntegerField(default= 0)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = QuestionManager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ("forum:detail", kwargs={"pk":self.pk})



class Answer(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	#qn = models.ForeignKey(Question)
	content_type = models.ForeignKey(ContentType, related_name='answers', on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey("content_type", "object_id")
	answer = models.TextField(help_text='Separate by a Comma')
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.owner.username

	def get_absolute_url(self):
		return reverse ("forum:detail", kwargs={"pk":self.pk})
