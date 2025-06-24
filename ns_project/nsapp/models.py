from django.db import models
from sst2.fields import StateField

class StudentModel(models.Model):
	name = models.CharField(max_length=40)
	state = StateField()
	
	def __str__(self):
		return self.name
