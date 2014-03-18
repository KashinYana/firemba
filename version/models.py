from django.db import models

# Create your models here.

class Version(models.Model):
	version = models.IntegerField()
	total = models.IntegerField()
	success = models.IntegerField()
	def __unicode__(self):
		return str(self.version) + " " + str(self.total) + " " + str(self.success)
