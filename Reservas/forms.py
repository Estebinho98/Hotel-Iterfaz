from django import forms
from .models import Rooms, Services, Booking, Booking_Marriage, Booking_Family




class DateInput(forms.DateInput):
    input_type = 'text'
    

class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class BookingForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=DateInput(attrs={'class': 'datepicker'}))
    exit_date = forms.DateField(widget=DateInput(attrs={'class': 'datepicker'}))
    
    services = forms.ModelMultipleChoiceField(
        queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Booking
        fields = '__all__'

class Booking_MarriageForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=DateInput(attrs={'class': 'datepicker'}))
    exit_date = forms.DateField(widget=DateInput(attrs={'class': 'datepicker'}))

    services = forms.ModelMultipleChoiceField(
        queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Booking_Marriage
        fields = '__all__'

class Booking_FamilyForm(forms.ModelForm):
    arrival_date = forms.DateField(widget=DateInput(attrs={'class': 'datepicker'}))
    exit_date = forms.DateField(widget=DateInput(attrs={'class': 'datepicker'}))

    services = forms.ModelMultipleChoiceField(
        queryset=Services.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Booking_Family
        fields = '__all__'