from django.db import models
from staffs.models import Staff
import datetime

class Day_hour (models.Model):
	staff = models.ForeignKey('staffs.Staff')
	day = models.DateField()
	hours = models.DecimalField(max_digits=3,decimal_places=1)
	
	def __unicode__ (self):
		return self.staff.name + '_worked_' + str(self.hours) + '_hours_on_' + self.day.strftime("%d-%m-%Y")
# Create your models here.
