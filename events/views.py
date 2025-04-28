import pdb;
from django.shortcuts import redirect, render
from .models import EventCategory, Events, Schedule, Ticket, TicketType
from .forms import CategoryForm, EventForm, ScheduleForm, TicketForm, TicketTypeForm

# Home Page
def home_view(request):
    events = Events.objects.all()
    return render(request, 'eventsApp/home.html', {'events':events})

#Category
def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    return render(request, 'eventsApp/settings/add_category.html', {'category_form':form})

def category_list(request):
    categories = EventCategory.objects.all()
    return render(request, 'eventsApp/settings/categories_list.html', {'categories':categories})

#Ticket
def create_ticket(request):
    form = TicketTypeForm()
    if request.method == 'POST':
        form = TicketTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    return render(request, 'eventsApp/settings/add_ticket.html', {'ticket_form':form})

def ticket_list(request):
    ticket = TicketType.objects.all() 
    return render(request, 'eventsApp/settings/ticket_list.html', {'ticket':ticket})

def events_list(request):
    events = Schedule.objects.all().select_related('event')
    # for e in events:
    #     schedule = Schedule.objects.filter(event_id=e)
    # pdb.set_trace()
    return render(request, 'eventsApp/event_list.html', {'events':events})

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

def event_details(request, event_id):
    event = Events.objects.get(id=event_id)
    schedule = Schedule.objects.get(event=event_id)
    ticket = Ticket.objects.get(event=event_id)
    return render(request, 'eventsApp/event_details.html', {'event':event, 'schedule':schedule, 'ticket':ticket})
