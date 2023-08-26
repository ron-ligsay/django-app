from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Command to do........'

    def add_argument(self, parser):
        pass
        
    def handle(self, *args, **options):
        try:
            # your logic here
            print("I am here")
            
        except Exception as e:
            CommandError(repr(e))
