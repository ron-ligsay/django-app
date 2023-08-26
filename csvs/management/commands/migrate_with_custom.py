from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run makemigrations, migrate, and a custom command'

    def handle(self, *args, **options):
        # Run makemigrations and migrate commands
        call_command('makemigrations')
        call_command('migrate')

        # Run your custom command
        call_command('mycommand')  # Replace with your custom command's name

        self.stdout.write(self.style.SUCCESS('Migration and custom command completed successfully'))
