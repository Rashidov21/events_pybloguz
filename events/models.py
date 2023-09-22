from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=250,blank=True)
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Tags" 

class Speaker(models.Model):
    name = models.CharField(max_length=100,blank=True)
    position = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='speakers/')
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Speakers" 

EVENT_TYPES = (
    ('boshlovchilar','Boshlovchilarga'),
    ('tajribalilar','Tajribalilarga'),
    ('barcha','Barcha uchun'),
)

class Event(models.Model):
    title = models.CharField(max_length=250,blank=True)
    tag = models.ManyToManyField(Tag, related_name='tags')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, blank=True)
    event_datetime = models.DateTimeField(blank=True)
    duration = models.CharField(max_length=100,blank=True)
    places = models.CharField(max_length=10, blank=True, default="cheklanmagan")
    about_event_short = models.TextField()
    about_event_plain = models.TextField()
    event_card_image = models.ImageField('380x480px',upload_to='event_cover',blank=True)
    event_cover_image = models.ImageField('1440x800px',upload_to='event_cover',blank=True)
    
    
    
    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Events" 
        

class Leads(models.Model):
    name = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=100,blank=True)
    age = models.CharField(max_length=10,blank=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='event_leads')
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Leads" 