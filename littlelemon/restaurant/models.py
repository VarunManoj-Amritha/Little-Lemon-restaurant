from django.db import models

# Create your models here.
# Booking Model
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self): 
        return f'{self.name} for {self.no_of_guests} guests on {self.booking_date.strftime("%Y-%m-%d")}'

# Menu Model
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'