from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('categories/create/', views.create_category, name="create_category"),
    path('categories/', views.category_list, name="category_list"),
    path('ticket/create/', views.create_ticket, name="create_ticket"),
    path('ticket/', views.ticket_list, name="ticket_list"),
    path('events/', views.events_list, name="events_list"),
    path('events/create/', views.create_event, name="create_event"),

    path('events/<int:event_id>/schedule/', views.event_schedule, name="schedule"),
]
