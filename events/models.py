from django.db import models

# Create your models here.
class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TicketType(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
#Events
class Events(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    class Status(models.TextChoices):
        ACTIVE = "active"
        EXPIRED = "expired"
    status = models.CharField(max_length=8, choices=Status)
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
    type = models.ForeignKey(TicketType, on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    ticket_qty = models.IntegerField()
    desc = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type