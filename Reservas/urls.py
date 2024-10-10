from django.urls import path, include
from . import views



urlpatterns = [
    
    path('home/', views.home, name='Home'),
    path('rooms/', views.room_list, name='Room-List'),
    path('rooms/<int:pk>/', views.room_detail, name='Room-Detail'),
    path('services/', views.services_list, name='Services-List'),
    path('services/<int:pk>/', views.services_detail, name='Service-Detail'),
    path('bookings/', views.booking_list, name='Booking-List'),
    path('bookings/<int:pk>/', views.booking_detail, name='Booking-Detail'),
    path('bookings-marriage/', views.booking_marriage_list, name='Booking-Marriage-List'),
    path('bookings-marriage/<int:pk>/', views.booking_marriage_detail, name='Booking-Marriage-Detail'),
    path('bookings-family/', views.booking_family_list, name='Booking-Family-List'),
    path('bookings-family/<int:pk>/', views.booking_family_detail, name='Booking-Family-Detail'),
    path('bookings/new/', views.booking_create, name='Booking-Create'),
    path('bookings-marriage/new/', views.booking_marriage_create, name='Booking-Marriage-Create'),
    path('bookings-family/new/', views.booking_family_create, name='Booking-Family-Create'),
   



]