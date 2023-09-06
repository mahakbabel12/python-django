from django.db import models

# Create your models here.
class student_details(models.Model):
    username =models.CharField(max_length=15)
    email =models.EmailField(max_length=50)
    address =models.CharField(max_length=30)
    state =models.CharField(max_length=20)
    pin_code = models.IntegerField()
    
    



    


    