from datetime import timedelta
from django.utils import timezone
from controllers.models import Controller

def update_controller_health():
    controllers = Controller.objects.all()

    for controller in controllers:
        if controller.updated_date < timezone.now() - timedelta(minutes=5):
            controller.health = False
            controller.save()

