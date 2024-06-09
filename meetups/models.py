from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 255)

    def __str__(self):
        return f"{self.name} ({self.address})"
    
class Participant(models.Model):
    email = models.EmailField(unique = True)


    def __str__(self):
        return self.email

class Meetups(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(unique = True)
    description = models.TextField()
    organizer = models.EmailField()
    date = models.DateField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    participant = models.ManyToManyField(Participant, blank=True)

    class Meta:
        verbose_name_plural = 'Meetup'

    def __str__(self):
        return self.title