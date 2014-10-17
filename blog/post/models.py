from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	date_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title