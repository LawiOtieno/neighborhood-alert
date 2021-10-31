from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.

# NeighborHood

class NeighborHood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey('Profile',on_delete=CASCADE,related_name='administrator')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    population = models.IntegerField(null=True,blank = True)
    police_contact = models.IntegerField(null=True,blank = True)
    hospital_contact = models.IntegerField(null=True,blank = True)
    image = CloudinaryField('image')

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    def __str__(self):
        return self.name


# Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)
    bio =models.TextField(null=True)
    profile_picture =CloudinaryField('image')
    location =models.CharField(max_length=60,blank=True,null=True)
    neighborhood = models.ForeignKey('NeighborHood', on_delete=SET_NULL,null=True, related_name='people', blank=True)
    

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
