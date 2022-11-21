from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver

from .models import Profile , BusinessProfile
from django.contrib.auth.models import User

@receiver(post_save , sender=User)
def createProfile(sender , instance , created , **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username ,
            email = user.email , 
            name = user.first_name,
        )

@receiver(post_delete , sender=Profile)
def deleteUser(sender , instance , **kwargs):
    user = instance.user
    user.delete()

@receiver(post_save , sender=Profile)
def createBusinessProfile(sender , instance , created , **kwargs):
    if created:
        user = instance
        bProfile = BusinessProfile.objects.create(
            user = user , 
            username = user.username ,
            email = user.email , 
            name = user.name,
            location = user.location , 
            id = user.id , 
            created = user.created , 
            profilepic = user.profilepic
        )

@receiver(post_delete , sender=BusinessProfile)
def deleteUser(sender , instance , **kwargs):
    user = instance.user
    user.delete()