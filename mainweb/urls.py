from django.urls import path
from . import views

app_name = 'mainweb'

urlpatterns = [
path('', views.Home_view, name='homepage'),
path('about', views.About_view, name='aboutpage'),
path('projects', views.Projects_view, name='projectspage'),
path('project/<str:pk>/', views.Projectview, name='project'),
path('services', views.Services_view, name='servicespage'),
path('service/<str:pk>/', views.serviceDetail, name='service'),
path('team', views.Team_view, name='teampage'),
path('team12/<str:pk>/', views.singleTeam, name='team12'),
path('contacts', views.Contacts_view, name='contactus'),
path('events', views.eventView, name='events'),
path('event/<str:pk>/', views.Event, name='event'),
]