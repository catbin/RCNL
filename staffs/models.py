from django.db import models
import datetime

class Staff(models.Model):
	name = models.CharField(max_length = 20)
	tel = models.CharField(max_length = 10)
	tfn = models.CharField(max_length = 9, blank = True, null=True)
	serve_date = models.DateField(null = True, blank = True)
	def __unicode__ (self):
		return self.name

class Salary(models.Model):
	staff = models.ForeignKey('Staff')
	salary = models.DecimalField(max_digits=4, decimal_places=2)
	effective_date = models.DateField()
	is_activate = models.BooleanField()

	def __unicode__ (self):
		s = self.staff.name + '_$' + str(self.salary)+ '_from_' + self.effective_date.strftime("%d-%m-%Y")
		if self.is_activate :
                	return '*'+s
		return s

class Shop(models.Model):
	shop_name = models.CharField(max_length = 20)
	
	def __unicode__ (self):
		return self.shop_name

class Employement (models.Model):
	staff = models.ForeignKey('Staff')
	shop = models.ForeignKey('Shop')
	
	def __unicode__ (self):
		return self.staff.name +"@"+self.shop.shop_name
	
class Day_hour (models.Model):
	staff = models.ForeignKey('Staff')
	day = models.DateField()
	hours = models.DecimalField(max_digits=3,decimal_places=1)
	
	def __unicode__ (self):
		return self.staff.name + '_worked_' + str(self.hours) + '_hours_on_' + self.day.strftime("%d-%m-%Y")