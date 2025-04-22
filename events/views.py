from django.shortcuts import redirect, render
from .models import EventCategory, Events, TicketType
from .forms import CategoryForm, EventForm, ScheduleForm, TicketTypeForm

# Home Page
def home_view(request):
    return render(request, 'eventsApp/home.html')

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
    events = Events.objects.all()
    return render(request, 'eventsApp/event_list.html', {'events':events})

def create_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            event_id = (Events.objects.last()).id
            return redirect('schedule', event_id)
    return render(request, 'eventsApp/event_form.html', {'event_form':form})

def event_schedule(request, event_id):
    event = Events.objects.get(id=event_id)
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=event_id)
        if form.is_valid():
            form.save()
            return redirect('schedule', event_id)
    return render(request, 'eventsApp/schedule.html', {'schedule':form})
