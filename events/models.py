from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
#Events
class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True, upload_to="posters/")
    is_published = models.BooleanField(default=False)
    class Status(models.TextChoices):
        ACTIVE = "active"
        EXPIRED = "expired"
    status = models.CharField(max_length=8, choices=Status, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Schedule(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event
    
class Ticket(models.Model):
    name = models.CharField(max_length=100, default="Free")
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    ticket_qty = models.IntegerField(default=1)
    desc = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class OrderTicket(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event

