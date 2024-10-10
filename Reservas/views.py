from django.shortcuts import render, get_object_or_404, redirect
from .models import Rooms, Services, Booking, Booking_Marriage, Booking_Family
from .forms import RoomsForm, ServicesForm, BookingForm,Booking_MarriageForm, Booking_FamilyForm
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view

# Create your views here.

def home(request):
    return render(request, 'index.html')


def room_list(request):
    rooms = Rooms.objects.all()
    return render(request,'room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Rooms, pk=pk)
    return render(request, 'single_room.html', {'room':room})

def services_list(request):
    services = Services.objects.all()
    return render(request,'services_list.html', {'services':services})

def services_detail(request, pk):
    service = get_object_or_404(Services, pk=pk)
    return render(request,'single_service.html', {'services':service}) 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request,'booking_list.html',{'bookings':bookings})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    total = booking.get_total()
    permission_classes = [IsAuthenticated]
    return render(request,'single_booking.html',{'booking':booking, 'total': total})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_marriage_list(request):
    bookings_marriage = Booking_Marriage.objects.all()
    permission_classes = [IsAuthenticated]
    return render(request,'booking_marriage_list.html',{'bookings_marriage':bookings_marriage})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_marriage_detail(request, pk):
    booking_marriage = get_object_or_404(Booking_Marriage, pk=pk)
    total = booking_marriage.get_total()
    permission_classes = [IsAuthenticated]
    return render(request,'single_booking_marriage.html',{'booking_marriage':booking_marriage, 'total': total})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_family_list(request):
    bookings_family = Booking_Family.objects.all()
    permission_classes = [IsAuthenticated]
    return render(request,'booking_family_list.html',{'bookings_family':bookings_family})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def booking_family_detail(request, pk):
    booking_family = get_object_or_404(Booking_Family, pk=pk)
    total = booking_family.get_total()
    permission_classes = [IsAuthenticated]
    return render(request,'single_booking_family.html', {'booking_family':booking_family, 'total':total})


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Booking-List')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form':form})


def booking_marriage_create(request):
    if request.method == 'POST':
        form = Booking_MarriageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Booking-Marriage-List')
    else:
        form = Booking_MarriageForm()
    return render(request, 'booking_marriage_form.html', {'form':form})


def booking_family_create(request):
    if request.method == 'POST':
        form = Booking_FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Booking-Family-List')
    else:
        form = Booking_FamilyForm()
    return render(request, 'booking_family_form.html', {'form':form})



