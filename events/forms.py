from time import timezone
from django import forms
from .models import EventCategory, Events, Schedule, Ticket, TicketType


class CategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = '__all__'
        labels = {
            'name':'Event Name',
            'desc':'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'e.g. Event category', 'class':'form-control my-2'}),
            'desc': forms.Textarea(attrs={'class':'form-control my-2', 'rows':'8'}),
        }

class TicketTypeForm(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = '__all__'
        labels = {
            'name':'Ticket type',
            'desc':'Description',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'e.g. Ticket type', 'class':'form-control my-2'}),
            'desc': forms.Textarea(attrs={'class':'form-control my-2', 'rows':'8'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('category','name','location','desc','poster')
        labels = {
            'category':'Ticket type',
            'name':'Event name',
            'location':'Address',
            'desc':'Description',
            'poster':'Event Poster image',
        }
        widgets = {
            'category': forms.Select(attrs={'class':'form-select my-2'}),
            'name': forms.TextInput(attrs={'placeholder':'', 'class':'form-control my-2'}),
            'location': forms.TextInput(attrs={'placeholder':'eg. Arusha Confrence Center', 'class':'form-control my-2'}),
            'desc': forms.Textarea(attrs={'class':'form-control my-2', 'rows':'8'}),
            'poster': forms.FileInput(attrs={'class':'form-control my-2'})
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('start_date','start_time','end_date','end_time')
        labels = {
            'start_date':'Start Date',
            'start_time':'Start Time',
            'end_date':'End Date',
            'end_time':'End Time',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'dateinput form-control my-2', 'type': 'date'} ),
            'start_time': forms.TimeInput(attrs={'class':'form-control my-2', 'type': 'time'}),
            'end_date': forms.DateInput(attrs={'class':'form-control my-2', 'type': 'date'} ),
            'end_time': forms.TimeInput(attrs={'class':'timeinput form-control my-2', 'type': 'time'}),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('type','price','ticket_qty','desc')
        labels = {
            'type':'Ticket',
            'price':'Price',
            'ticket_qty':'Ticket quantity',
            'desc':'Description',
        }
        widgets = {
            'type': forms.Select(attrs={'class':'form-select my-2'} ),
            'price': forms.NumberInput(attrs={'class':'form-control my-2'}),
            'ticket_qty': forms.NumberInput(attrs={'class':'form-control my-2'} ),
            'desc': forms.Textarea(attrs={'class':'form-control my-2', 'rows':'8'}),
        }