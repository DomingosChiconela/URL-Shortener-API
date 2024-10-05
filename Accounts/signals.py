from django.dispatch import receiver
from django.db.models.signals import post_save

from. models import Users
from rolepermissions.roles import assign_role


@receiver(post_save, sender=Users)
def define_permissoes(sender,instance,created, ** kwargs):
    if created:
        if instance.status =="N":
            assign_role(instance,'normal')
           
        if instance.status =="A":
            assign_role(instance,'Admin')
           