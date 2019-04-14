from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'base.html')



def visitors(request):
	return render(request, 'visitors.html')


def hotel(request):
	return render(request, 'hotel.html')



def staff(request):
	return render(request, 'staff.html')