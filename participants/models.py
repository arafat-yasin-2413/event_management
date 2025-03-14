from django.db import models
from events.models import Event

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    event = models.ManyToManyField(Event)
    
    def __str__(self):
        return self.name
    