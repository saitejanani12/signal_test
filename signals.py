import time
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import datetime,threading
from testapp.models import LogEntry

@receiver(pre_save, sender=User)
def pre_save_handler(sender, instance, **kwargs):
    print(f"Signal received. Starting delay at {datetime.datetime.now()}")
    time.sleep(5)
    print(f"Signal handler completed at {datetime.datetime.now()}")

@receiver(pre_save, sender=User)
def pre_save_handler(sender, instance, **kwargs):
    print(f"Signal Handler Thread: {threading.current_thread().name}")
    print(f"Signal handler for user: {instance.username}")


@receiver(post_save, sender=User)
def log_user_creation(sender, instance, created, **kwargs):
    if created:
        LogEntry.objects.create(message=f"User {instance.username} created")
        print("Signal handler: Log entry created.")