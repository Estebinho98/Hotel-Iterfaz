from django.contrib import admin
from .models import Rooms, Services, Booking, Booking_Marriage, Booking_Family
# Register your models here.
admin.site.register(Rooms)
admin.site.register(Services)
admin.site.register(Booking)
admin.site.register(Booking_Marriage)
admin.site.register(Booking_Family)
