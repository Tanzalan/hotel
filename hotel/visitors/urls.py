from django.urls import path

from . import views

app_name = 'visitors'
urlpatterns = [
	path('', views.index, name='index'),
	path('visitors/', views.visitors, name='visitors'),
	path('hotel/', views.hotel, name='hotel'),
	path('staff/', views.staff, name='staff'),
]