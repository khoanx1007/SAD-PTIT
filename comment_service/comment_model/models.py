from django.db import models
# Create your models here.
class comment_detail (models.Model):

	### followings are the fields of our table.
	product_id = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	comment = models.CharField(max_length=255)

	### It will help to print the values.
	def __str__(self):
		return '%s %s %s' % (self.product_id, self.username, self.comment)
