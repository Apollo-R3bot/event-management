import pdb;
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .decorators import allowed_users
from .models import EventCategory, Events, OrderTicket, Schedule, Ticket
from .forms import AttendeeForm, CategoryForm, CreateUserForm, EventForm, ScheduleForm, TicketForm


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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def category_list(request):
    categories = EventCategory.objects.all()
    return render(request, 'eventsApp/settings/categories_list.html', {'categories':categories})

# List Events
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','organizer'])
def events_list(request):
    events = Schedule.objects.all().select_related('event')
    return render(request, 'eventsApp/event_list.html', {'events':events})

# Create Event
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','organizer'])
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
            # event_id = (Events.objects.last()).id
            return redirect('events_list')
    return render(request, 'eventsApp/event_form.html', {'event_form':event_form, 'schedule_form':schedule_form, 'ticket_form':ticket_form})


def event_details_and_create_ticket(request, event_id):
    event = Events.objects.get(id=event_id)
    schedule = Schedule.objects.get(event=event_id)
    ticket = Ticket.objects.filter(event=event_id)
    form = AttendeeForm()
    if request.method == 'POST':
        ticket_type = request.POST.get('ticket')
        order_ticket = Ticket.objects.get(id=ticket_type)

        form = AttendeeForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            orderForm = OrderTicket(event=event, ticket=order_ticket, user=user)
            order_number = orderForm.save()

            attendee = form.save(commit=False)
            attendee.order = order_number
            attendee.save()
            return redirect('events_list')
    return render(request, 'eventsApp/event_details.html', {'event':event, 'schedule':schedule, 'tickets':ticket, 'attendee_form':form})


# Bookig Ticket
# Create Ticket (By adding Attendee)
def create_ticket(request):
    form = AttendeeForm()
    if request.method == 'POST':
        ticket = request.POST.get('ticket')
        form = AttendeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_details')
    return render(request, 'eventsApp/event_details.html', {'attendee_form':form})
