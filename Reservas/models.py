from django.db import models

# Create your models here.
class Rooms(models.Model):
    room = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.room

class Services(models.Model):
    services = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.services

class Booking(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    arrival_date = models.DateField()
    exit_date = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)

    def get_total(self):
        total = self.room.price
        for service in self.services.all():
            total += service.price
        return total

class Booking_Marriage(models.Model):
    Full_name_spouse1 = models.CharField(max_length=200)
    Full_name_spouse2 = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    arrival_date = models.DateField()
    exit_date = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)

    def get_total(self):
        total = self.room.price
        for service in self.services.all():
            total += service.price
        return total

class Booking_Family(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    members = models.IntegerField()
    arrival_date = models.DateField()
    exit_date = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    services = models.ManyToManyField(Services)

    def get_total(self):
        total = self.room.price
        for service in self.services.all():
            total += service.price
        return total


