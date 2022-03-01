""" Create/ Update User Profile """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccount(models.Model):
    """ User Profile Saved Details """
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    official_phone = models.CharField(max_length=15, null=True, blank=True)
    official_address_line1 = models.CharField(max_length=100,
                                              null=True, blank=True)
    official_address_line2 = models.CharField(max_length=100,
                                              null=True, blank=True)
    official_address_line3 = models.CharField(max_length=100,
                                              null=True, blank=True)
    official_town = models.CharField(max_length=100, null=True, blank=True)
    official_postcode = models.CharField(max_length=20, null=True, blank=True)
    official_country = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.profile)


"""
@receiver(post_save, sender=User)
def new_update_profile_info(sender, instance, new, **kwargs):
    if new:
        UserAccount.objects.create(profile=instance)
    instance.UserAccount.save()
"""
