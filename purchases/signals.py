from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LineItem


@receiver(post_save, sender=LineItem)
def edit_post_save(sender, instance, created, **kwargs):

    instance.Purchase.final_total()


@receiver(post_delete, sender=LineItem)
def delete_post_save(sender, instance, **kwargs):

    instance.Purchase.final_total()