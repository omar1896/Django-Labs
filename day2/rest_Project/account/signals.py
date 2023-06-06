from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
