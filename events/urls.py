from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),

    path('categories/create/', views.create_category, name="create_category"),
    path('categories/<int:cat_id>/delete', views.delete_category, name="delete_category"),
    path('categories/', views.category_list, name="category_list"),

    path('events/', views.events_list, name="events_list"),
    path('event/create/', views.create_event, name="create_event"),        
    path('event/<int:event_id>/update', views.update_event, name='update_event'), # Update
    path('event/<int:event_id>/delete', views.delete_event, name='delete_event'), # Delete

    path('event/<int:event_id>/ticket', views.ticket_list, name="ticket_list"), # View Ticket
    path('event/<int:event_id>/ticket/update', views.update_ticket, name='ticket_update'), # Update
    path('event/ticket/<int:ticket_id>/delete', views.delete_ticket, name='ticket_delete'), # Delete

    path('event/<int:event_id>/attendee', views.attendee_list, name="attendee_list"), # View Attendee
    path('event/<int:event_id>/attendee/update', views.update_attendee, name='attendee_update'), # Update
    path('event/attendee/<int:attendee_id>/delete', views.delete_attendee, name='attendee_delete'), # Delete

    path('event/my-order', views.booking_list, name="booking_list"), # View Order

    path('event/<int:event_id>/', views.event_details_and_create_ticket, name="event"),
]
