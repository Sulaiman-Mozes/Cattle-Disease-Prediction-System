from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 25)
	email = models.EmailField()
	comment = models.TextField()


	def __str__(self):
		return self.name


	#def get_absolute_url (self):
	#	return reverse ("contact:contact")