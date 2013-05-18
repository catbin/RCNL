from django.db import models

class User ( models.Model ):
        name = models.CharField( max_length = 60 ,blank = True,null = True)
        uname = models.CharField( max_length = 14, unique = True )
        email = models.EmailField( max_length = 75, unique = True )
        password = models.CharField( max_length = 256 )
        last_login = models.DateTimeField()
        privilage = models.IntegerField()

	def __unicode__ (self):
		return self.name
