from .models import Robot
from django.db.models.signals import post_save
from django.dispatch import receiver
from .send_email import send_email


@receiver(post_save, sender=Robot)
def check_availability_robot(sender, instance, created, **kwargs):
    if instance.available:
        send_email(instance)
