from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime,threading
from django.db import IntegrityError,transaction
from testapp.models import LogEntry
from django.core.exceptions import ObjectDoesNotExist

def test_signal(request):
    print(f"Starting save operation at {datetime.datetime.now()}")
    user = User(username='testuser')
    user.save()
    print(f"Save operation completed at {datetime.datetime.now()}")
    return HttpResponse("Signal test completed")

def test_signal_2(request):
    try:
        if not User.objects.filter(username='testuser_2').exists():
            user = User(username='testuser_2')
            user.save()
            return HttpResponse("User created and signal triggered.")
        else:
            return HttpResponse("User with this username already exists.")
    
    except IntegrityError as e:
        return HttpResponse(f"IntegrityError occurred: {e}")


def test_signal_transaction(request):
    try:
        with transaction.atomic():
            if not User.objects.filter(username='testuser_3').exists():
                user = User(username='testuser_3')
                user.save()
                try:
                    log_entry = LogEntry.objects.get(message=f"User testuser created")
                    print("View: Log entry found, proceeding to raise exception.")
                except ObjectDoesNotExist:
                    return HttpResponse("LogEntry not found after user creation.")
                raise IntegrityError("Deliberate transaction failure.")

            else:
                return HttpResponse("User 'testuser' already exists, skipping creation.")

    except IntegrityError as e:
        return HttpResponse(f"Transaction rolled back due to: {e}")

    return HttpResponse("Transaction succeeded.")