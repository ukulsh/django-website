from django.db import models

# Create your models here.


#aded models visitor
class Visitor(models.Model):
    name=models.TextField(max_length=30)
    
    inTime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
