from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),

    path('categories/create/', views.create_category, name="create_category"),
    path('categories/', views.category_list, name="category_list"),

    path('events/', views.events_list, name="events_list"),
    path('event/create/', views.create_event, name="create_event"),        
    path('event/<int:event_id>/update', views.update_event, name='update_event'), # Update

    path('event/<int:event_id>/ticket', views.ticket_list, name="ticket_list"),
    path('event/<int:event_id>/ticket', views.update_ticket, name='ticket'), # Ticket

    path('event/<int:event_id>/', views.event_details_and_create_ticket, name="event"),
]
