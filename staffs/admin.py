
from django.contrib import admin
from staffs.models import Staff, Salary, Employement, Shop

admin.site.register(Staff, Salary, Employement, Shop)


