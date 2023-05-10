from django.db import models

# Create your models here.


class cart_item(models.Model):
    username = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return '%s %s %s %s %s'%(self.username, self.product_id, self.quantity, self.price, self.status)