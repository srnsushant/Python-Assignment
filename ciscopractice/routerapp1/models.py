from django.db import models
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class RouterDetails(models.Model):
    class Meta:
        db_table = 'router_details'

    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=200)
    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
