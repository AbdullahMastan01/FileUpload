from django.db import models

class CSVfile_data(models.Model):

	name 			= models.CharField(("Name") ,max_length=50)
	sku 			= models.CharField(("sku") , max_length=100 ,unique=True)
	description 	= models.CharField(("Description") , max_length=500)

	class Meta:
		verbose_name_plural 		= "CSVfile_data"