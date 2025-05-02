from time import timezone
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Attendee, EventCategory, Events, OrderTicket, Schedule, Ticket

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']
        labels = {
            'username':'Username:',
            'email':'Email address:',
            'password1':'Password:',
        }
        


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
        fields = ('name','price','ticket_qty','desc')
        labels = {
            'name':'Name',
            'price':'Price (TZS)',
            'ticket_qty':'Ticket quantity',
            'desc':'Description',
        }
        widgets = {
            'type': forms.Select(attrs={'class':'form-select my-2'} ),
            'price': forms.NumberInput(attrs={'class':'form-control my-2'}),
            'ticket_qty': forms.NumberInput(attrs={'class':'form-control my-2'} ),
            'desc': forms.Textarea(attrs={'class':'form-control my-2', 'rows':'8'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderTicket
        fields = '__all__'
        labels = { 'ticket':'Ticket: '}
        widgets = { 'ticket': forms.RadioSelect(attrs={'class':'form-select my-2'} ) }

class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ('name','phone','email')
        labels = {
            'name':'Name',
            'phone':'Phone',
            'email':'Email',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control my-2'} ),
            'phone': forms.TextInput(attrs={'class':'form-control my-2'}),
            'email': forms.EmailInput(attrs={'class':'form-control my-2'} ),
        }