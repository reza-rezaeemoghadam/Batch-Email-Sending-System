from django.core.management.base import BaseCommand
from django.core.management import call_command

from src.base import INSTALLED_APPS

class Command(BaseCommand):
    help = 'Because of the custom folder structure there is a problem with django makmigrations and this will fix it.'

    def handle(self, *args, **kwargs):
        app_count = 0
        for app in INSTALLED_APPS:
            if "application" in app:
                app = app.split(".")[-1]
                call_command('makemigrations', app)
                self.stdout.write(self.style.SUCCESS(f"migration file for '{app}' successfully added."))
                app_count +=1
        # Implement your command logic here
        self.stdout.write(self.style.SUCCESS(f'A total of {app_count} migration files have been created.'))

