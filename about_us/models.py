from django.db import models

# Create your models here.

class AboutUs(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()

	class Meta:
		verbose_name= 'about us'
		verbose_name_plural= 'about us'

	def __str__(self):
		return self.title


class Members(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to= 'members/')

	class Meta:
		verbose_name='member'
		verbose_name_plural= 'member'

	def __str__(self):
		return self.name

