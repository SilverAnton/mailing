from django.apps import AppConfig
from time import sleep

class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        print("Sending Mails ..")
        from main.services import start_scheduler
        sleep(2)
        start_scheduler()
