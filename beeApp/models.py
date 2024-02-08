from django.db import models

# Create your models here.

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    state_of_origin = models.CharField(max_length=255)
    dob = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50)


    def __str__(self):

        return self.surname + "   " + self.first_name