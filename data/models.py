from django.db import models

# Create your models here.

class Data(models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	patronymic = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name + ", " + self.surname + ", "+ self.patronymic + ", " + self.phone + ", " + self.email
