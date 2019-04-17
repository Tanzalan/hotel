from django.shortcuts import render
from django.http import HttpResponse
from .models import Room, Booking
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.utils import timezone


def index(request):
	booking = BookingForm()
	# if request.method == 'POST':
	# 	booking = BookingForm(request.POST)
	# 	if booking.is_valid():
	context = {
		'form':booking
	}

	return render(request, 'index.html', context)


def info(request):

	return render(request, 'info.html')


def all_room(request):
	rooms = Room.objects.all()
	
	context = {
		'rooms' : rooms
	}
	return render(request, 'rooms.html', context)


def the_room(request, room_id):
	room = Room.objects.get(pk=room_id)
	print(room)
	context = {
		'room':room
	}

	return render(request, 'room.html', context)


def show_vacancies(request):
  return render(request, 'show_vacancies.html')

# @login_required(login_url="/login")
# def show_vacancies(request):
# 	f = BookingForm()
# 	if request.method == 'POST':
# 		f = BookingForm(request.POST)
# 		if f.is_valid():
# 			booking = f.save(commit=False)
# 			booking.customer = request.user
# 			# own made function gets the date.
# 			room = get_available_room(booking.start_date, booking.end_date)
# 			print(room)
# 			if room is None:
# 				# add flash message?
# 				# redirect to the booking page
# 				return redirect('visitors:booking')
# 			booking.room = room
# 			booking.save()
# 			# 
# 			# redirect to info page
# 		return redirect('visitors:show_vacancies')
# 	context = {
# 		'form':f
# 	}
# 	return render(request, 'show_vacancies.html', context)


# def show_vacancies(request):



# 	rooms = Booking.objects.exclude(start_date__isnull=True, end_date__isnull=True)
# 	print(rooms)
# 	context = {
# 		'rooms': rooms
# 	}



# 	return render(request, 'booking.html',context)


 # def show_vacancies(start_date='2019-03-01 10:00:00', end_date='20019-02-02 10:00:00'):

 #        '''get all rooms without bookings whose:

 #               start date is before C,

 #                   and end date is after C

 #               OR whose start date is on or after C

 #                   and start date is before D. '''

 #        free_rooms = Room.objects.exclude(

 #            Q(booking__start_date__lt=start_date,

 #              booking__end_date__gt=start_date) |

 #            Q(booking__start_date__gte=start_date,

 #              booking__start_date__lt=end_date))

 #        return free_rooms
 #        print(free_rooms)
 #        return render(request, 'booking.html',context)