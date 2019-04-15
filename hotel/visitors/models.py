from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Booking(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	room = models.ForeignKey('Room', on_delete=models.CASCADE)
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)


class Room(models.Model):
	room_number = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

