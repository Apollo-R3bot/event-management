import pdb;
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .decorators import allowed_users
from .models import EventCategory, Events, OrderTicket, Schedule, Ticket
from .forms import BookTicketForm, CategoryForm, CreateUserForm, EventForm, ScheduleForm, TicketForm


# Authentication
# Register User
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name="Customer")
                user.groups.add(group)

                error_message = "Account created successful for "+ username
                messages.success(request, error_message)
                return redirect('login')
        return render(request, 'eventsApp/register.html', {'register_form':form})

# Login
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next') or 'home'
                return redirect(next_url)
            else:
                error_message = "Invalid username or password.!"
                messages.error(request, error_message)
        return render(request, 'eventsApp/login.html')

# Logout
def logoutPage(request):
    logout(request)
    return redirect('login')

    
# Home Page
def home_view(request):
    events = Events.objects.all()
    return render(request, 'eventsApp/home.html', {'events':events})

#Create Category
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    return render(request, 'eventsApp/settings/add_category.html', {'category_form':form})


# List categories
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def category_list(request):
    categories = EventCategory.objects.all()
    return render(request, 'eventsApp/settings/categories_list.html', {'categories':categories})

# Delete category
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def delete_category(request, cat_id):
    category = get_object_or_404(EventCategory, pk=cat_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'eventsApp/settings/category_list.html')


# List Events
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def events_list(request):
    events = Schedule.objects.all().select_related('event')
    return render(request, 'eventsApp/settings/event_list.html', {'events':events})

# Create Event
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def create_event(request):
    event_form = EventForm()
    schedule_form = ScheduleForm()
    ticket_form = TicketForm()

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES)
        schedule_form = ScheduleForm(request.POST)
        ticket_form = TicketForm(request.POST)

        if event_form.is_valid() and schedule_form.is_valid() and ticket_form.is_valid():
            event = event_form.save()
            schedule = schedule_form.save(commit=False)
            schedule.event = event
            schedule.save()

            ticket = ticket_form.save(commit=False)
            ticket.event = event
            ticket.save()
            return redirect('events_list')

    return render(request, 'eventsApp/settings/event_form.html', {'event_form':event_form, 'schedule_form':schedule_form, 'ticket_form':ticket_form})


#Create Event Ticket
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def update_ticket(request, event_id=None):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    return render(request, 'eventsApp/settings/add_ticket.html', {'ticket_form':form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def ticket_list(request, event_id):
    ticket = Ticket.objects.filter(event=event_id)
    event = Events.objects.get(id=event_id)

    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.event = event 
            ticket.save()
            return redirect('ticket_list', event_id)
    return render(request, 'eventsApp/settings/event_ticket.html', {'ticket_form':form, 'tickets':ticket})

# DELETE Ticket Type
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list', ticket.event.id)
    return render(request, 'eventsApp/settings/event_ticket.html', {'tickets':ticket})

# Update Event
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def update_event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Events, pk=event_id)     
        schedule_instance = Schedule.objects.get(event=instance.id)
    else:
        instance = None

    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES, instance=instance)
        schedule_form = ScheduleForm(request.POST, instance=schedule_instance)

        if event_form.is_valid() and schedule_form.is_valid():
            event = event_form.save()
            schedule = schedule_form.save(commit=False)
            schedule.event = event
            schedule.save()
            return redirect('events_list')
    else:
        event_form = EventForm(instance=instance)
        schedule_form = ScheduleForm(instance=schedule_instance)
        ticket_form = TicketForm()

    context = {'event_form':event_form, 'schedule_form':schedule_form, 'event':event_id}
    return render(request, 'eventsApp/settings/event_update.html', context)

# DELETE Event
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin','Organizer'])
def delete_event(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('events_list')
    return render(request, 'eventsApp/settings/event_list.html')

# Bookig Ticket
# Create Ticket (By adding Attendee)
def event_details_and_create_ticket(request, event_id):
    event = Events.objects.get(id=event_id)
    schedule = Schedule.objects.get(event=event_id)
    ticket = Ticket.objects.filter(event=event_id)

    form = BookTicketForm()
    if request.method == 'POST':
        if request.user.is_authenticated:
            ticket_type = request.POST.get('ticket')
            order_ticket = Ticket.objects.get(id=ticket_type)
            form = BookTicketForm(request.POST)
            if form.is_valid():
                user_id = request.user.id
                user = User.objects.get(id=user_id)

                instance = form.save(commit=False)
                instance.event = event
                instance.ticket = order_ticket
                instance.user = user

                instance.save()
                return redirect('event', event_id)
        else:
            return redirect('login')
    return render(request, 'eventsApp/event_details.html', {'event':event, 'schedule':schedule, 'tickets':ticket, 'bock_ticket_form':form})

def attendee_list(request, event_id):
    attendee = OrderTicket.objects.filter(event=event_id)
    event = Events.objects.get(id=event_id)
    return render(request, 'eventsApp/settings/event_order.html', {'attendees':attendee})

def update_attendee(request):
    return render(request)

def delete_attendee(request):
    return render(request)

# Booking
def booking_list(request):
    order = OrderTicket.objects.all().select_related('event','ticket')
    # event = Events.objects.get(id=event_id)
    return render(request, 'eventsApp/settings/event_order.html', {'orders':order})