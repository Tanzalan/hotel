from django.urls import path

from . import views

app_name = 'visitors'
urlpatterns = [
	path('', views.index, name='index'),
	path('rooms/', views.all_room, name='all_room'),
	path('room/<int:room_id>', views.the_room, name='the_room'),
	path('dates/', views.show_vacancies, name='show_vacancies'),
	path('info/', views.info, name='info'),

]