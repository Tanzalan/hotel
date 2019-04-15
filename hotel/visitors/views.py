from django.shortcuts import render

from django.http import HttpResponse

from .models import Room
# Create your views here.

def index(request):
	return render(request, 'base.html')



def visitors(request):
	rooms = Room.objects.all()
	
	context = {
		'rooms' : rooms
	}
	return render(request, 'visitors.html', context)


def hotel(request):
	return render(request, 'hotel.html')



def staff(request):
	return render(request, 'staff.html')