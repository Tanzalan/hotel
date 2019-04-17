from django import forms
from django.forms.widgets import SelectDateWidget

from .models import Booking

class BookingForm(forms.ModelForm):
	start_date = forms.DateField(label='Start Date',widget=SelectDateWidget)
	end_date = forms.DateField(widget=SelectDateWidget,label='End Date')

	class Meta:
		model = Booking
		fields = ['start_date', 'end_date', 'room']
		widgets = {'room': forms.HiddenInput}
		exclude = ['room']