from django.db import models

# Create your models here.
class Bookings(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.CharField(max_length=50)
    Date=models.DateField()
    No_of_people=models.IntegerField()
    Message=models.TextField()


    class Meta:
        db_table="bookings"