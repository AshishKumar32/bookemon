from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    time_start=models.TimeField()
    time_end=models.TimeField()
    bookings=models.IntegerField()
    thumbnail = CloudinaryField('image')
    booked=ArrayField(models.IntegerField(),default= list, size = 20)


class ticket(models.Model):
    movie=models.CharField(max_length=200)
    book_time=models.TimeField()
    user=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    nos=models.IntegerField()
    seats=ArrayField(models.IntegerField(),default= list)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tickets = ArrayField(models.IntegerField(),default= list)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
